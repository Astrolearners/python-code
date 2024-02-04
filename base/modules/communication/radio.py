import colorama
import serial
import time

from modules.helpers.logger import logger

class radio():
    def __init__(self, port):
        self.log = logger("radio")
        self.port = port
        colorama.init()

        self.log.debug("Connecting to gps module...")
        try:
            self.radio = serial.Serial(port, baudrate=9600)
        except Exception as e:
            self.log.critical(f"Failed to contact gps module! Error: {e}")
            # exit()

    def radioSendCommand(self, command):
        self.log.debug(f"Sending command {command}...")
        try:
            self.radio.write(command.encode())
            retries = 0
            while self.radio.readline().decode().find(command) != -1:
                retries += 1
                if retries >= 10:
                    self.log.critical("Didn't get response from cansat!")
                    return
                time.sleep(0.5)
            reponse = self.radio.readline().decode()
            self.log.info(f"Got response from cansat! Response: {reponse}")
        except Exception as e:
            self.log.error(f"Failed to send command! Error {e}")

    def commandShell(self):
        command = str(input(colorama.Fore.BLUE + "Enter command" + colorama.Fore.RED + " >>> " + colorama.Fore.LIGHTBLACK_EX))
        if command == "readPiTemp":
            self.radioSendCommand(command)
        elif command == "getBmeData":
            self.radioSendCommand(command)
        elif command == "getGPSData":
            self.radioSendCommand(command)
        elif command == "readAccelerometer":
            self.radioSendCommand(command)
        elif command == "abort":
            confirm = str(input(colorama.Back.RED + "WARNING! The abort command will kill the main python script resulting in mission fail! If you are sure you want to procceed write 'Yes, do as I say!': "))
            if confirm == "Yes, do as I say!":
                self.log.critical("Aborting mission!")
                self.radioSendCommand(command)
        elif command == "exit":
            self.log.warn("Exiting...")
            time.sleep(0.5)
            exit()
        elif command == "help":
            print(colorama.Fore.RED + "Available Commands:\n\n" + colorama.Fore.LIGHTBLACK_EX + "readPiTemp" + colorama.Fore.BLUE + " - " + colorama.Fore.GREEN + "Read the raspberry pi cpu temperature\n" + colorama.Fore.LIGHTBLACK_EX + "getBmeData" + colorama.Fore.BLUE + " - " + colorama.Fore.GREEN + "Read data from the bme sensor\n " + colorama.Fore.LIGHTBLACK_EX + "getGPSData" + colorama.Fore.BLUE + " - " + colorama.Fore.GREEN + "Read data from the gps module\n " + colorama.Fore.LIGHTBLACK_EX + "buzzerBeep" + colorama.Fore.BLUE + " - " + colorama.Fore.GREEN + "Beep the active buzzer 5 times with 1 second sleep\n" + colorama.Fore.LIGHTBLACK_EX + "readAccelerometer" + colorama.Fore.BLUE + " - " + colorama.Fore.GREEN + "Read the data from the accelerometer\n" + colorama.Fore.LIGHTBLACK_EX + "abort" + colorama.Fore.BLUE + " - " + colorama.Fore.GREEN + "Abort the mission\n" + colorama.Fore.LIGHTBLACK_EX + "exit" + colorama.Fore.BLUE + " - " + colorama.Fore.GREEN + "Exit the program\n" + colorama.Fore.LIGHTBLACK_EX + "help" + colorama.Fore.BLUE + " - " + colorama.Fore.GREEN + "Print this help command")
        else:
            print(colorama.Fore.RED + f"Cannot find command {command}" + colorama.Fore.LIGHTBLACK_EX)