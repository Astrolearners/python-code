from modules.helpers.logger import logger
from modules.sensors.bme680 import bme
from time import sleep

log_level = 3

class main_code():
    def __init__(self, log_level):
        self.log = logger("main", log_level)

        self.log.info("Initializing sensors...")
        try:
            self.log.debug("Initializing bme680 sensor...")
            self.bme680 = bme(log_level)
        except Exception as e:
            self.log.error("Failed to initialize the bme680 sensor...")

        self.log.info("Creating data arrays...")
        self.bme_array = []

    def getBmeData(self):
        try:
            self.log.info("Getting data from bme680 sensor...")
            self.bme_array(self.bme680.getHumdity())
            self.bme_array(self.bme680.getTemp())
            self.bme_array(self.bme680.getPressure())
            self.bme_array(self.bme680.getGas())
        except Exception as e:
            self.log.error(f"Error getting data! Error: {e}")

main = main_code(log_level)

while True:
    main.log.debug("Hello, World!")
    sleep(1)