from time import sleep
from datetime import datetime

from modules.helpers.logger import logger
from modules.sensors.bme680 import bme
from modules.communication.gps import gps
from modules.other.buzzer import buzzer
from modules.other.rpi_temp import rpi_temp
from modules.schemas.schemas import *

class main_code():
    def __init__(self):
        self.log = logger("main")

        self.log.info("Initializing helper components...")
        try:
            self.log.debug("Initializing buzzer...")
            self.buzzer = buzzer("passive")
        except Exception as e:
            self.log.error(f"Failed to initialize the buzzer module! Error: {e}")
        try:
            self.log.debug("Initializing rpi_temp...")
            self.rpi_temp = rpi_temp()
        except Exception as e:
            self.log.error(f"Failed to initialize the rpi_temp module! Error: {e}")

        self.log.info("Initializing sensors...")
        try:
            self.log.debug("Initializing bme680 sensor...")
            self.bme680 = bme()
        except Exception as e:
            self.log.critical(f"Failed to initialize the bme680 sensor! Error: {e}")
            self.buzzer.beep(2, 1)

        self.log.info("Initializing modules...")
        try:
            self.log.debug("Initializing gps module...")
            self.gps = gps()
        except Exception as e:
            self.log.critical(f"Failed to initialize the gps module! Error: {e}")
            self.buzzer.beep(3, 1)

        self.log.info("Creating data arrays...")
        self.bme_data = bme_schema
        self.gps_data = gps_schema
        self.main_data = main_schema

    def getBmeData(self):
        try:
            self.log.info("Getting data from bme680 sensor...")
            self.bme_data["temp"] = self.bme680.getTemp()
            self.bme_data["humidity"] = self.bme680.getHumidity()
            self.bme_data["pressure"] = self.bme680.getPressure()
            self.bme_data["gas"] = self.bme680.getGas()
        except Exception as e:
            self.log.error(f"Error getting data! Error: {e}")

    def getGpsData(self):
        try:
            self.log.info("Getting data from gps module...")
            for i in range(2):
                self.gps.gpsUpdate()
                self.gps_data["latitude"] = self.gps.getLatitude()
                self.gps_data["longitude"] = self.gps.getLongitude()
                self.gps_data["altitude"] = self.gps.getAltitude()
                self.gps_data["speed"] = self.gps.getSpeed()
                self.gps_data["satellites"] = self.gps.getSatellites()
                self.gps_data["fixQuality"] = self.gps.getFixQuality()
        except Exception as e:
            self.log.error(f"Error getting data! Error: {e}")

    def run(self):
        self.log.info("Ready!")
        self.buzzer.beep(0.5, 2)
        try:
            while True:
                self.log.info("Getting data...")
                self.buzzer.beep(0.5, 1)
                time = datetime.now()
                self.getGpsData()
                self.getBmeData()
                self.main_data["time"] = f"{time.hour}:{time.minute}:{time.second}"
                self.main_data["bme"] = self.bme_data
                self.main_data["gps"] = self.gps_data
                self.main_data["rpi_temp"] = self.rpi_temp.getCpuTemp()
                print(self.main_data)
        except KeyboardInterrupt:
            self.log.warn("Detected keyboard interrupt shutting down...")
            sleep(0.5)
            exit()

main_code().run()
