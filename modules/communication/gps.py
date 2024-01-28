from time import sleep
import adafruit_gps
import serial

from modules.helpers.logger import logger

class gps():
    def __init__(self):
        self.log = logger("gps")

        self.uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=10)
        try:
            self.gps = adafruit_gps.GPS(self.uart, debug=False)
        except Exception as e:
            self.log.critical(f"Failed to contact with gps module. Cannot continue with program! Error: {e}")
            # Scary
            exit()

        self.log.debug("Setting communication method with sensor...")
        self.gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
        self.gps.send_command(b"PMTK220,1000")

    def gpsUpdate(self):
        self.gps.update()
        return None
    
    def getLatitude(self):
        if self.gps.has_fix:
            return self.gps.latitude
        else:
            return None
    
    def getLongitude(self):
        if self.gps.has_fix:
            return self.gps.longitude
        else:
            return None
    
    def getAltitude(self):
        if self.gps.has_fix:
            return self.gps.altitude_m
        else:
            return None
        
    def getSpeed(self):
        if self.gps.has_fix:
            return self.gps.speed_knots
        else:
            return None
        
    def getSatellites(self):
        if self.gps.has_fix:
            return self.gps.satellites
        else:
            return None
        
    def getFixQuality(self):
        if self.gps.has_fix:
            return self.gps.fix_quality
        else:
            return None