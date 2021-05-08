#!/usr/bin/env python3
import pandas as pd
import numpy as np
from datetime import datetime,timedelta
import sys
import logging


def load_data(timetable_path,data_path):
    df_timetables = pd.read_csv(timetable_path) #site_id,opening_datetime,closing_datetime
    df_data = pd.read_csv(data_path) #sensor_identifier,sensor_name,site_id,last_record_datetime
    # merging with only the necessary column 
    df_full = pd.merge(df_data,df_timetables[['opening_datetime','closing_datetime','site_id']],on='site_id')
    df_full['last_record_datetime'] =  pd.to_datetime( df_full.last_record_datetime )
    df_full['opening_datetime'] = pd.to_datetime( df_full.opening_datetime )
    df_full['closing_datetime'] = pd.to_datetime( df_full.closing_datetime )
    return df_full.sort_values('last_record_datetime',ascending=False)
def lvl_filter(x,now):
    # the alerts delta_t
    t_2H = timedelta(hours=2)
    t_1D = timedelta(days=1)
    t_2D = timedelta(days=2)
    # delta_t beween now and last_record_datetime
    delta = now - x.last_record_datetime 
    # if the 'now' is withine the site closing time to opening time we dont have an alert
    # if closing_datetime or opening_datetime  is nat we continue with the alert checking
    if  ( 
        ( not pd.isnull(x.closing_datetime) and  not pd.isnull(x.opening_datetime) ) and 
        (  now > x.closing_datetime and now < x.opening_datetime ) 
        ): return 'ok'
    if  (delta > t_2D) :return '3'
    if  (delta > t_1D) :return '2'
    if  (delta > t_2H) :return '1'
    else: return 'ok'

def format_output(data):
    return \
        "Sensor {sensor_name:11} with identifier {sensor_identifier:4} triggers an alert at {alert_date} with level {alert} with last data recorded at {last_record_datetime}"\
        .format(
        sensor_name=data.sensor_name,
        sensor_identifier=data.sensor_identifier,
        alert_date=data.alert_date,
        alert=data.alert,
        last_record_datetime=data.last_record_datetime
    )

if __name__ == '__main__': 
    #cmdline settings
    if len(sys.argv) != 2 : 
        logging.error(' ./run.py <date::isoformat> | now')
        exit()
    if sys.argv[1].lower() == 'now' :
        now = datetime.now()
    else:
        try : now  = datetime.fromisoformat(sys.argv[1])
        except ValueError : 
            logging.error(' ./run.py <date::isoformat> | now')
            exit()
    # loading,flitering and printing the data
    df = load_data('data/timetables.csv','data/data.csv') #load function
    df['alert']= df.apply(lambda x : lvl_filter(x,now),axis=1) # 
    df['alert_date'] = np.where(df['alert']!='ok',now,pd.NaT)

    for r in df.loc[df.alert!='ok'].itertuples(False):
       print(format_output(r))