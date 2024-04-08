# System libraries
from datetime import datetime
import threading

# Helpers
from modules.helpers.logger import logger
from modules.helpers.csv_handler import csvHandler

# Sensors
from modules.sensors.bme680 import bme
from modules.sensors.accelerometer import accelerometer
from modules.sensors.camera import camera

# Communication
from modules.communication.gps import gps
from modules.communication.radio import radio

# Other
from modules.other.buzzer import buzzer
from modules.other.rpi_temp import rpi_temp

# Schemas
from modules.schemas.schemas import *

# Constants
from modules.constants.constats import *

class main_code():
    def __init__(self):
        self.log = logger("main")

        self.running = True
        self.find = False

        self.log.info("Initializing helper components...")

        try:
            self.log.debug("Initializing debug_buzzer...")
            self.debug_buzzer = buzzer(21, "passive")
        except Exception as e:
            self.log.error(f"Failed to initialize the debug_buzzer module! Error: {e}")

        try:
            self.log.debug("Initializing find_buzzer...")
            self.find_buzzer = buzzer(20, "active")
        except Exception as e:
            self.log.error(f"Failed to initialize the active_buzzer module! Error: {e}")

        try:
            self.log.debug("Initializing rpi_temp...")
            self.rpi_temp = rpi_temp()
        except Exception as e:
            self.log.error(f"Failed to initialize the rpi_temp module! Error: {e}")
     
        try:
            self.log.debug("Initializing csv handler...")
            self.csv_handler = csvHandler()
        except Exception as e:
            self.log.error(f"Failed to initialize the csv_handler module! Error: {e}")

        self.log.info("Initializing sensors...")

        try:
            self.log.debug("Initializing bme680 sensor...")
            self.bme680 = bme()
        except Exception as e:
            self.log.critical(f"Failed to initialize the bme680 sensor! Error: {e}")
            self.debug_buzzer.beep(2, 1)

        try:
            self.log.debug("Initializing accelerometer sensor...")
            self.accelerometer = accelerometer()
        except Exception as e:
            self.log.critical(f"Failed to initialize the accelerometer sensor! Error: {e}")
            self.debug_buzzer.beep(2, 1)

        self.log.info("Initializing modules...")

        try:
            self.log.debug("Initializing gps module...")
            self.gps = gps()
        except Exception as e:
            self.log.critical(f"Failed to initialize the gps module! Error: {e}")
            self.debug_buzzer.beep(3, 1)

        try:
            self.log.debug("Initializing camera...")
            self.camera = camera()
            self.camera.start()
        except Exception as e:
            self.log.critical(f"Failed to initialize the camera module! Error: {e}")
            self.debug_buzzer.beep(3, 1)

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
            self.log.error(f"Error getting bme data! Error: {e}")

    def getGpsData(self):
        try:
            self.log.info("Getting data from gps module...")
            self.gps.gpsUpdate()
            self.gps_data["latitude"] = self.gps.getLatitude()
            self.gps_data["longitude"] = self.gps.getLongitude()
            self.gps_data["altitude"] = self.gps.getAltitude()
            self.gps_data["speed"] = self.gps.getSpeed()
            self.gps_data["satellites"] = self.gps.getSatellites()
            self.gps_data["fixQuality"] = self.gps.getFixQuality()
        except Exception as e:
            self.log.error(f"Error getting gps data! Error: {e}")

    def getAccelerometerData(self):
        try:
            self.log.info("Getting data from accelerometer sensor...")
            self.accelerometer_data["accelerometer"]["X"] = self.accelerometer.getAccelerometer()[0]
            self.accelerometer_data["accelerometer"]["Y"] = self.accelerometer.getAccelerometer()[1]
            self.accelerometer_data["accelerometer"]["Z"] = self.accelerometer.getAccelerometer()[2]
            self.accelerometer_data["magnetometer"]["X"] = self.accelerometer.getMagnetometer()[0]
            self.accelerometer_data["magnetometer"]["Y"] = self.accelerometer.getMagnetometer()[1]
            self.accelerometer_data["magnetometer"]["Z"] = self.accelerometer.getMagnetometer()[2]
        except Exception as e:
            self.log.error(f"Error getting accelerometer data! Error: {e}")

    def safeShutdown(self):
        self.log.warn("Safe shutdown...")
        self.running = False
        self.camera.stop()
        self.csv_handler.saveDataframe()

    def findBuzeer(self):
        while self.find:
            self.find_buzzer.beep(0.5, 1)

    def run(self):
        self.log.info("Ready!")
        self.debug_buzzer.beep(0.5, 2)

        try:
            while self.running:
                self.log.info("Getting data...")
                self.debug_buzzer.beep(0.5, 1)

                # Time
                time = datetime.now()

                # Sensor Data
                self.getGpsData()
                self.getBmeData()
                self.getAccelerometerData()

                # Parse data to array
                self.main_data["time"] = f"{time.hour}:{time.minute}:{time.second}"
                self.main_data["bme"] = self.bme_data
                self.main_data["gps"] = self.gps_data
                self.main_data["accelerometer"] = self.accelerometer_data
                self.main_data["rpi_temp"] = self.rpi_temp.getCpuTemp()

                # Camera
                self.camera.capture()

                # Parse to csv
                self.csv_handler.addData(self.main_data)
                self.csv_handler.saveDataframe()
                
                # Log
                self.log.debug(self.main_data)
        except KeyboardInterrupt:
            self.safeShutdown()

main = main_code()
r = radio()

running = False
find = False

while True:
    command = r.get()

    try:
        if command.find("start") != -1:
            if not running:
                thread = None
                main.running = True
                thread = threading.Thread(target=main.run).start()
                running = True
                r.send("start: ok")
            else:
                r.send("start: fail: already running")

        elif command.find("stop") != -1:
            if running:
                main.safeShutdown()
                r.send("stop: ok")
            else:
                r.send("stop: fail: not running")

        elif command.find("restart") != -1:
            main.safeShutdown()
            thread = None
            main.running = True
            thread = threading.Thread(target=main.run).start()
            running = True
            r.send("restart: ok")

        elif command.find("getdata") != -1:
            if running:
                data = main.main_data
                r.send(f"getdata: ok: {data}")
            else:
                r.send("getdata: fail: not running")

        elif command.find("findstart") != -1:
            if not find:
                find_thread = None
                main.find = True
                find_thread = threading.Thread(target=main.findBuzeer).start()
                r.send("findstart: ok")
            else:
                r.send("findstart: fail: already in find mode")

        elif command.find("findstop") != -1:
            if find:
                main.find = False
                r.send("findstop: ok")
            else:
                r.send("findstop: fail: not in find mode")

        elif command.find("ping") != -1:
            r.send("pong")

    except Exception as e:
        r.send(f"error: {e}")

# DONE 🎊🎊🎊