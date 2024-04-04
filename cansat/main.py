from time import sleep
from datetime import datetime
import os
import threading

from modules.helpers.logger import logger
from modules.sensors.bme680 import bme
from modules.sensors.accelerometer import accelerometer
from modules.sensors.camera import camera
from modules.communication.gps import gps
from modules.communication.radio import radio
from modules.other.buzzer import buzzer
from modules.other.rpi_temp import rpi_temp
from modules.schemas.schemas import *

class main_code():
    def __init__(self):
        self.log = logger("main")
        self.capture_path = f"{os.getcwd()}/captures"

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
        try:
            self.log.debug("Initializing accelerometer sensor...")
            self.accelerometer = accelerometer()
        except Exception as e:
            self.log.critical(f"Failed to initialize the accelerometer sensor! Error: {e}")
            self.buzzer.beep(2, 1)

        self.log.info("Initializing modules...")
        try:
            self.log.debug("Initializing gps module...")
            self.gps = gps()
        except Exception as e:
            self.log.critical(f"Failed to initialize the gps module! Error: {e}")
            self.buzzer.beep(3, 1)
        try:
            self.log.debug("Initializing camera...")
            if not os.path.exists(self.capture_path):
                try:
                    os.mkdir(self.capture_path)
                except Exception as e:
                    self.log.error(f"Failed to create capture path! Error: {e}")
                    raise "Failed to create capture path!"
            self.camera = camera(self.capture_path)
            self.camera.start()
        except Exception as e:
            self.log.critical(f"Failed to initialize the camera module! Error: {e}")
            self.buzzer.beep(3, 1)

        self.log.info("Creating data arrays...")
        self.bme_data = bme_schema
        self.gps_data = gps_schema
        self.accelerometer_data = accelerometer_schema
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

    def getAccelerometerData(self):
        try:
            self.log.info("Getting data from accelerometer sensor...")
            self.accelerometer_data["accelerometer"]["X"] = self.accelerometer.getAccelerometer()[0]
            self.accelerometer_data["accelerometer"]["Y"] = self.accelerometer.getAccelerometer()[1]
            self.accelerometer_data["accelerometer"]["Z"] = self.accelerometer.getAccelerometer()[2]
            self.accelerometer_data["magnetometer"]["X"] = self.accelerometer.getAccelerometer()[0]
            self.accelerometer_data["magnetometer"]["Y"] = self.accelerometer.getAccelerometer()[1]
            self.accelerometer_data["magnetometer"]["Z"] = self.accelerometer.getAccelerometer()[2]
        except Exception as e:
            self.log.error(f"Error getting data! Error: {e}")

    def setData(self):
        self.log.info("Getting data...")
        self.buzzer.beep(0.5, 1)
        time = datetime.now()
        self.getGpsData()
        self.getBmeData()
        self.getAccelerometerData()
        self.main_data["time"] = f"{time.hour}:{time.minute}:{time.second}"
        self.main_data["bme"] = self.bme_data
        self.main_data["gps"] = self.gps_data
        self.main_data["accelerometer"] = self.accelerometer_data
        self.main_data["rpi_temp"] = self.rpi_temp.getCpuTemp()
        self.camera.capture()

    def run(self):
        self.log.info("Ready!")
        self.buzzer.beep(0.5, 2)
        try:
            while True:
                self.setData()
                print(self.main_data)
        except KeyboardInterrupt:
            self.log.warn("Detected keyboard interrupt shutting down...")
            self.camera.stop()
            exit()

radio_com = radio()
main = main_code()

thread = threading.Thread(main.run())

while True:
    command = radio_com.get()
    if command == "start":
        print("Start command!")
        thread.start()
        radio_com.send("start: ok")
    elif command == "stop":
        print("Stop command!")
        thread.stop()
        radio_com.send("stop: ok")
    elif command == "restart":
        print("Restart command!")
        thread.stop()
        sleep(1)
        thread.start()
        radio_com.send("restart: ok")
    elif command == "getData":
        print("Get data command!")
        radio_com.send(f"getData: {main.main_data}")
    elif command == "ping":
        print("Ping command!")
        radio_com.send("pong")