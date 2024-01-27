from time import sleep
from datetime import datetime

from modules.helpers.logger import logger
from modules.sensors.bme680 import bme
from modules.communication.gps import gps

class main_code():
    def __init__(self):
        self.log = logger("main")

        self.log.info("Initializing sensors...")
        try:
            self.log.debug("Initializing bme680 sensor...")
            self.bme680 = bme()
        except Exception as e:
            self.log.error(f"Failed to initialize the bme680 sensor! Error: {e}")

        try:
            self.log.debug("Initializing gps module...")
            self.gps = gps()
        except Exception as e:
            self.log.error(f"Failed to initialize the gps module! Error: {e}")

        self.log.info("Creating data arrays...")
        self.bme_data = {"Temperature": None, "Humidity": None, "Pressure": None, "GAS": None}
        self.gps_data = {"Latitude": None, "Longitude": None, "Altitude": None, "Speed": None, "Satellites": None, "Fix Quality": None}

    def getBmeData(self):
        try:
            self.log.info("Getting data from bme680 sensor...")
            self.bme_data["Temperature"] = self.bme680.getTemp()
            self.bme_data["Humidity"] = self.bme680.getHumidity()
            self.bme_data["Pressure"] = self.bme680.getPressure()
            self.bme_data["GAS"] = self.bme680.getGas()
        except Exception as e:
            self.log.error(f"Error getting data! Error: {e}")

    def getGpsData(self):
        try:
            self.log.info("Getting data from gps module...")
            self.gps_data["Latitude"] = self.gps.getLatitude()
            self.gps_data["Longitude"] = self.gps.getLongitude()
            self.gps_data["Altitude"] = self.gps.getAltitude()
            self.gps_data["Speed"] = self.gps.getSpeed()
            self.gps_data["Satellites"] = self.gps.getSatellites()
            self.gps_data["Fix Quality"] = self.gps.getFixQuality()
        except Exception as e:
            self.log.error(f"Error getting data! Error: {e}")

    def run(self):
        while True:
            print("hi")


main_code().run()