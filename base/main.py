import time
import os

from modules.communication.radio import radio
from modules.helpers.logger import logger

from modules.helpers.commandHandler import commandHandler


class main_code():
    def __init__(self):
        self.log = logger("main")

        self.log.info("Initializing radio communication...")
        self.radio = radio("COM4")

        self.log.info("Initializing commandHanlder...")
        self.handler = commandHandler()

    def sendCommand(self):
        command = self.handler.inputShell()
        if command != None:
            if command == "help":
                self.handler.helpCommand()
            elif command == "exit":
                self.log.warn("Shutting down...")
                exit()
            elif command == "clear":
                if os.name == "nt":
                    os.system("cls")
                else:
                    os.system("clear")
            else:
                print(command)
                self.radio.sendCommand(command)
        else:
            pass

    def run(self):
        try:
            self.log.debug("Launching command shell over radio...")
            while True:
                self.sendCommand()
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("")
            self.log.warn("Detected keyboard interrupt, shutting down...")


main_code().run()
