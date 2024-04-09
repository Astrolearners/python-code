import colorlog
import logging
import sys
from modules.constants.constats import log_file

class logger():
    def __init__(self, name, path=log_file, level=logging.DEBUG):
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
        self.formatter = colorlog.ColoredFormatter("%(name)s: %(asctime)s - %(log_color)s%(levelname)-8s%(reset)s > %(message)s", datefmt="%d-%m-%Y %H:%M:%S", reset=True, log_colors={
            "DEBUG":    "cyan",
            "INFO":     "green",
            "WARNING":  "yellow",
            "ERROR":    "red",
            "CRITICAL": "purple",
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
        self.logger.warning(text)

    def error(self, text):
        self.logger.error(text)

    def debug(self, text):
        self.logger.debug(text)

    def critical(self, text):
        self.logger.critical(text)