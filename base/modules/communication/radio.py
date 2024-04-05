import serial

from modules.helpers.logger import logger

class radio():
    def __init__(self, port, bol="$", eol="/r", max_retries=5):
        self.log = logger("radio")
        self.port = port
        self.bol = bol
        self.eol = eol
        self.max_retries = max_retries

        self.log.debug("Connecting to radio module...")
        try:
            self.radio = serial.Serial(port, baudrate=9600)
            self.radio.rts = False
            self.radio.timeout = 10
        except Exception as e:
            self.log.critical(f"Failed to contact radio module! Error: {e}")

    def sendCommand(self, command):
        self.log.debug(f"Sending command {command}...")
        try:
            self.radio.write(f"{self.bol}{command}{self.eol}".encode())
            response = self.radio.readline().decode()
            if response != "":
                self.log.info(
                    f"Got response from cansat! Response: {response}")
            else:
                self.log.warn("Timeout reached!")
        except Exception as e:
            self.log.error(f"Failed to send command! Error {e}")
