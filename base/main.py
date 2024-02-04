import time

from modules.communication.radio import radio
from modules.helpers.logger import logger

class main_code():
    def __init__(self):
        self.log = logger("main")

        self.log.info("Initializing radio communication...")
        self.radio = radio("COM3")

    def run(self):
        try:
            self.log.debug("Launching command shell over radio...")
            while True:
                self.radio.commandShell()
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("")
            self.log.warn("Detected keyboard interrupt, shutting down...")

main_code().run()