from modules.libraries.softwareserial import softwareSerial
from modules.helpers.logger import logger

class radio():
    def __init__(self):
        self.log = logger("radio")
        
        self.log.debug("Creating software serial connection...")
        self.radio = softwareSerial(23, 24, 9600)

        self.log.debug("Software serial ready!")

    def send(self, message):
        try:
            self.log("Sending message...")
            self.radio.write(message)
        except Exception as e:
            self.error(f"Error in sending message! Error: {e}")

    def get(self):
        try:
            self.log.info("Waiting for message...")
            message = self.radio.read()
            if message != None:
                return message
            return ""
        except Exception as e:
            self.log.error(f"Error in getting message! Error: {e}")
            return ""
