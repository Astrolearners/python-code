import colorama
import datetime

class logger():
    def __init__(self, name):
        colorama.init()
        self.name = name
        
    def info(self, text):
        date_time = datetime.datetime.now()
        print(f"{self.name}: {date_time} - {colorama.Fore.BLUE} info {colorama.Fore.RESET} >\t{text}")

    def warn(self, text):
        date_time = datetime.datetime.now()
        print(f"{self.name}: {date_time} - {colorama.Fore.YELLOW} warn {colorama.Fore.RESET} >\t{text}")

    def error(self, text):
        date_time = datetime.datetime.now()
        print(f"{self.name}: {date_time} - {colorama.Fore.RED} error {colorama.Fore.RESET} >\t{text}")

    def debug(self, text):
        date_time = datetime.datetime.now()
        print(f"{self.name}: {date_time} - {colorama.Fore.GREEN} debug {colorama.Fore.RESET} >\t{text}")

    def critical(self, text):
        date_time = datetime.datetime.now()
        print(f"{self.name}: {date_time} - {colorama.Back.RED}critical{colorama.Back.RESET} >\t{text}")