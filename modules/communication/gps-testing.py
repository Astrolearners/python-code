from time import sleep
import adafruit_gps
import serial

uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=10)
gps = adafruit_gps.GPS(uart, debug=False)

gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
gps.send_command(b"PMTK220,1000")

def gpsGetData():
    data = []
    if gps.has_fix:
        data.append(gps.longitude_degrees)
        data.append(gps.latitude_degrees)
        data.append(gps.altitude_m)
        data.append(gps.speed_knots)
        data.append(gps.satellites)
        data.append(gps.fix_quality)
    else:
        return None
    
while True:
    gps.update()
    print(gpsGetData())
    sleep(1)