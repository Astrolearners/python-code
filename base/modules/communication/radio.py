import serial

from modules.helpers.logger import logger

class radio():
    def __init__(self, port ):
        self.log = logger("radio")
        self.port = port

        self.log.debug("Connecting to radio module...")
        try:
            self.radio = serial.Serial(port, baudrate=9600)
            self.radio.rts = False
            self.radio.timeout = 10
        except Exception as e:
            self.log.critical(f"Failed to contact radio module! Error: {e}")

    def getData(self):
        self.info("Getting data...")
        try:
            received = self.radio.readline().decode()
            if received != "":
                self.log.info(
                    f"Got data from cansat! Data: {received}")
            else:
                self.log.warn("Timeout reached!")
        except Exception as e:
            self.log.error(f"Failed to get data! Error {e}")

    def config(self, frequency=433000, dataRate=9600, power=9, uartRate=3, seriesCheckout=0):
        try:
            self.log.info(f"Configuring radio with parameters: {frequency} {dataRate} {power} {uartRate} {seriesCheckout}")
            self.radio.write(f"WR {frequency} {dataRate} {power} {uartRate} {seriesCheckout}")
        except Exception as e:
            self.log.error(f"Error sending data to gps module! Error: {e}")
