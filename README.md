# Modem API

## NOTE: 
```
In order to run the program, you will need to set up a python virtual environment with Flask and pyserial installed.
For Windows, make sure to update COM3 to correct COM connection
For Linux, make sure to update the COM to /dev/[usb]; this may require changing the read/write permissions - e.g. $sudo chmod a+rw /dev/ttyUSB0

```
## Test Serial Port [Windows]
```
Use Postman
```

## Test Serial Port [Linux]
```
curl -X POST -H "Content-Type: application/json" -d '{"message": "d1:1/d2:2"}' http://localhost:5000/passCounts
```

## Run the program
```
python ModemApi.py
```
