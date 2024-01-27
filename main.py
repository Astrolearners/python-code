from modules.helpers.logger import logger
from modules.sensors.bme680 import bme
from time import sleep

class main_code():
    def __init__(self):
        self.log = logger("main")

        self.log.info("Initializing sensors...")
        try:
            self.log.debug("Initializing bme680 sensor...")
            self.bme680 = bme()
        except Exception as e:
            self.log.error("Failed to initialize the bme680 sensor...")

        self.log.info("Creating data arrays...")
        self.bme_array = []

    def getBmeData(self):
        try:
            self.log.info("Getting data from bme680 sensor...")
            self.bme_array.append(self.bme680.getHumidity())
            self.bme_array.append(self.bme680.getTemp())
            self.bme_array.append(self.bme680.getPressure())
            self.bme_array.append(self.bme680.getGas())
        except Exception as e:
            self.log.error(f"Error getting data! Error: {e}")

main = main_code()

while True:
    main.log.debug("Hello, World!")
    sleep(1)