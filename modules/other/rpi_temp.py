from time import sleep
import subprocess

from modules.helpers.logger import logger

class rpi_temp():
    def __init__(self):
        self.log = logger("rpi_temp")

    def getCpuTemp(self):
        self.log.debug("Running vcgencmd command...")
        return float(subprocess.run(["vcgencmd", "measure_temp"], stdout=subprocess.PIPE).stdout.decode("utf-8").split("=")[1].split("'")[0])
