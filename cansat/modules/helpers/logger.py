import colorlog
import logging
import sys
from datetime import datetime

from modules.constants.constats import log_path

def setFileName():
    date_time = datetime.now()
    file_name = date_time.strftime("%d_%m_%y-%H-%M-%S.log")
    return f"{log_path}/{file_name}"

class logger():
    def __init__(self, name, path=setFileName(), level=logging.DEBUG):
        self.name = name
        self.path = path
        self.level = level

        # Create logger
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(self.level)

        # Create handlers
        self.file_logger = logging.FileHandler(self.path, mode="a", encoding="utf-8")
        self.console_logger = logging.StreamHandler(sys.stdout)

        # Create formatter
        self.formatter = colorlog.ColoredFormatter("%(log_color)s%(name)s: %(asctime)s -  %(levelname)s >\t%(message)s", datefmt="%d-%m-%Y %H:%M:%S", reset=True, log_colors={
            "DEBUG":    "cyan",
            "INFO":     "green",
            "WARNING":  "yellow",
            "ERROR":    "red",
            "CRITICAL": "bold_red",
	    },)
        
        # Set formatters
        self.file_logger.setFormatter(self.formatter)
        self.console_logger.setFormatter(self.formatter)

        # Add handler to logger
        self.logger.addHandler(self.file_logger)
        self.logger.addHandler(self.console_logger)

    def info(self, text):
        self.logger.info(text)

    def warn(self, text):
        self.logger.warn(text)

    def error(self, text):
        self.logger.error(text)

    def debug(self, text):
        self.logger.debug(text)

    def critical(self, text):
        self.logger.critical(text)