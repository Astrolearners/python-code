import colorama

from modules.communication.radio import radio
from modules.helpers.logger import logger


class main_code():
    def __init__(self):
        self.log = logger("main")
        colorama.init(autoreset=True)

        self.log.info("Initializing radio communication...")
        try:
            self.radio = radio(input(colorama.Fore.BLUE + "Enter Port >> " + colorama.Fore.RESET))
            self.radio.config()
        except Exception as e:
            self.log.error(f"Error initializing radio module! Error: {e}")
            
    def run(self):
        try:
            self.log.info("Radio ready! Starting...")
            while True:
                self.log.info("Getting data...")
                self.radio.getData()
        except KeyboardInterrupt:
            self.log.warn("Keyboard interrupt! Shutting down...")
            exit(0)

main_code().run()
