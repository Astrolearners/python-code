import serial
import time

from modules.helpers.logger import logger


class radio():
    def __init__(self, port):
        self.log = logger("radio")
        self.port = port
        self.max_retries = 5

        self.log.debug("Connecting to gps module...")
        try:
            self.radio = serial.Serial(port, baudrate=9600)
            self.radio.setRTS(0)
        except Exception as e:
            self.log.critical(f"Failed to contact gps module! Error: {e}")

    def radioSendCommand(self, command):
        self.log.debug(f"Sending command {command}...")
        try:
            self.radio.write(command.encode())
            retries = 0
            response = ""
            while response.find(command) == -1:
                response = self.radio.readline().decode()
                retries += 1
                if retries >= self.max_retries + 1:
                    self.log.critical("Didn't get response from cansat!")
                    return
                time.sleep(0.1)
            self.log.info(f"Got response from cansat! Response: {response}")
        except Exception as e:
            self.log.error(f"Failed to send command! Error {e}")
