### How to run 
`$ python3 run.py <date | 'now'>`
- Date en format iso (**2021-05-05** , **2021-05-05 15:52:0**) pour simuler le test sur un date precise
- Token **'now'** pour verifier avec la datetime actuel 
### example
```bash
$ ./run.py '2021-05-05 15:51:00'
Sensor sensor_222  with identifier  222 triggers an alert at 2021-05-05 15:52:00 with level 1 with last data recorded at 2021-05-04 15:52:00
Sensor sensor_221  with identifier  221 triggers an alert at 2021-05-05 15:52:00 with level 1 with last data recorded at 2021-05-04 15:52:00
Sensor sensor_223  with identifier  223 triggers an alert at 2021-05-05 15:52:00 with level 2 with last data recorded at 2021-05-04 15:17:00
Sensor sensor_193  with identifier  193 triggers an alert at 2021-05-05 15:52:00 with level 2 with last data recorded at 2021-05-04 15:17:00
Sensor sensor_64   with identifier   64 triggers an alert at 2021-05-05 15:52:00 with level 2 with last data recorded at 2021-05-04 15:17:00
Sensor sensor_63   with identifier   63 triggers an alert at 2021-05-05 15:52:00 with level 2 with last data recorded at 2021-05-04 15:17:00
Sensor sensor_198  with identifier  198 triggers an alert at 2021-05-05 15:52:00 with level 2 with last data recorded at 2021-05-04 15:17:00
Sensor sensor_62   with identifier   62 triggers an alert at 2021-05-05 15:52:00 with level 2 with last data recorded at 2021-05-04 15:17:00
Sensor sensor_191  with identifier  191 triggers an alert at 2021-05-05 15:52:00 with level 2 with last data recorded at 2021-05-04 15:17:00
Sensor sensor_56   with identifier   56 triggers an alert at 2021-05-05 15:52:00 with level 2 with last data recorded at 2021-05-04 15:17:00
Sensor sensor_192  with identifier  192 triggers an alert at 2021-05-05 15:52:00 with level 2 with last data recorded at 2021-05-04 15:17:00
Sensor sensor_193  with identifier  193 triggers an alert at 2021-05-05 15:52:00 with level 2 with last data recorded at 2021-05-04 15:17:00
Sensor sensor_189  with identifier  189 triggers an alert at 2021-05-05 15:52:00 with level 2 with last data recorded at 2021-05-04 15:17:00
Sensor sensor_194  with identifier  194 triggers an alert at 2021-05-05 15:52:00 with level 2 with last data recorded at 2021-05-04 15:17:00
Sensor sensor_172  with identifier  172 triggers an alert at 2021-05-05 15:52:00 with level 2 with last data recorded at 2021-05-04 15:17:00
Sensor sensor_73   with identifier   73 triggers an alert at 2021-05-05 15:52:00 with level 2 with last data recorded at 2021-05-04 15:17:00
Sensor sensor_71   with identifier   71 triggers an alert at 2021-05-05 15:52:00 with level 2 with last data recorded at 2021-05-04 15:17:00
...
```
```bash
$ ./run.py now                  
Sensor sensor_222  with identifier  222 triggers an alert at 2021-05-08 23:33:39.643982 with level 3 with last data recorded at 2021-05-04 15:52:00
Sensor sensor_221  with identifier  221 triggers an alert at 2021-05-08 23:33:39.643982 with level 3 with last data recorded at 2021-05-04 15:52:00
Sensor sensor_223  with identifier  223 triggers an alert at 2021-05-08 23:33:39.643982 with level 3 with last data recorded at 2021-05-04 15:17:00
Sensor sensor_193  with identifier  193 triggers an alert at 2021-05-08 23:33:39.643982 with level 3 with last data recorded at 2021-05-04 15:17:00
Sensor sensor_64   with identifier   64 triggers an alert at 2021-05-08 23:33:39.643982 with level 3 with last data recorded at 2021-05-04 15:17:00
Sensor sensor_63   with identifier   63 triggers an alert at 2021-05-08 23:33:39.643982 with level 3 with last data recorded at 2021-05-04 15:17:00
Sensor sensor_198  with identifier  198 triggers an alert at 2021-05-08 23:33:39.643982 with level 3 with last data recorded at 2021-05-04 15:17:00
Sensor sensor_62   with identifier   62 triggers an alert at 2021-05-08 23:33:39.643982 with level 3 with last data recorded at 2021-05-04 15:17:00
Sensor sensor_191  with identifier  191 triggers an alert at 2021-05-08 23:33:39.643982 with level 3 with last data recorded at 2021-05-04 15:17:00
Sensor sensor_56   with identifier   56 triggers an alert at 2021-05-08 23:33:39.643982 with level 3 with last data recorded at 2021-05-04 15:17:00
Sensor sensor_192  with identifier  192 triggers an alert at 2021-05-08 23:33:39.643982 with level 3 with last data recorded at 2021-05-04 15:17:00
Sensor sensor_193  with identifier  193 triggers an alert at 2021-05-08 23:33:39.643982 with level 3 with last data recorded at 2021-05-04 15:17:00
Sensor sensor_189  with identifier  189 triggers an alert at 2021-05-08 23:33:39.643982 with level 3 with last data recorded at 2021-05-04 15:17:00
Sensor sensor_194  with identifier  194 triggers an alert at 2021-05-08 23:33:39.643982 with level 3 with last data recorded at 2021-05-04 15:17:00
Sensor sensor_172  with identifier  172 triggers an alert at 2021-05-08 23:33:39.643982 with level 3 with last data recorded at 2021-05-04 15:17:00
Sensor sensor_73   with identifier   73 triggers an alert at 2021-05-08 23:33:39.643982 with level 3 with last data recorded at 2021-05-04 15:17:00
Sensor sensor_71   with identifier   71 triggers an alert at 2021-05-08 23:33:39.643982 with level 3 with last data recorded at 2021-05-04 15:17:00
...
```