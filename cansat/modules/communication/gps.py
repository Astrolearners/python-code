import pynmea2 

from modules.helpers.logger import logger
from modules.libraries.softwareserial import softwareSerial

class gps():
    def __init__(self):
        self.log = logger("gps")
        
        self.log.debug("Creating software serial connection...")
        self.gps = softwareSerial(5, 6, 9600)

        self.log.debug("Software serial ready!")

        self.receivedData = ""

    def getSerialData(self):
        self.log.info("Getting serial data...")
        self.receivedData = self.gps.read()

    def parseData(self):
        self.log.info("Parsing data to pynmea2...")
        data = pynmea2.parse(self.receivedData)
        return data
    
    def getData(self):
        self.log.info("Getting data from gps...")
        self.getSerialData()
        if self.receivedData.find("GPGGA") != -1:
            return self.parseData()
        return None