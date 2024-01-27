from time import sleep
from datetime import datetime

from modules.helpers.logger import logger
from modules.sensors.bme680 import bme
from modules.communication.gps import gps
from modules.other.buzzer import buzzer
from modules.other.rpi_temp import rpi_temp

class main_code():
    def __init__(self):
        self.log = logger("main")

        self.log.info("Initializing sensors...")
        try:
            self.log.debug("Initializing bme680 sensor...")
            self.bme680 = bme()
        except Exception as e:
            self.log.error(f"Failed to initialize the bme680 sensor! Error: {e}")

        self.log.info("Initializing modules...")
        try:
            self.log.debug("Initializing gps module...")
            self.gps = gps()
        except Exception as e:
            self.log.error(f"Failed to initialize the gps module! Error: {e}")
        try:
            self.log.debug("Initializing buzzer...")
            self.buzzer = buzzer()
        except Exception as e:
            self.log.error(f"Failed to initialize the buzzer module! Error: {e}")
        try:
            self.log.debug("Initializing rpi_temp...")
            self.rpi_temp = rpi_temp()
        except Exception as e:
            self.log.error(f"Failed to initialize the rpi_temp module! Error: {e}")

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
        self.log.info("Ready!")
        self.buzzer.beep(0.5, 2)
        while True:
            self.log.info("Getting data...")
            self.buzzer.beep(0.5, 1)
            self.getGpsData()
            self.getBmeData()
            print(f"GPS Data: {self.gps_data}")
            print(f"BME Data: {self.bme_data}")
            print(f"Raspberry CPU Temp {self.rpi_temp.getCpuTemp()}")

main_code().run()