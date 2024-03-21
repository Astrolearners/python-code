import board
import adafruit_lsm303_accel
import adafruit_lsm303dlh_mag

from modules.helpers.logger import logger

class accelerometer():
    def __init__(self):
        self.log = logger("accelerometer")

        self.log.debug("Initializing i2c communication...")
        self.i2c = board.I2C()

        self.log.debug("Initializing magnetometer module...")
        self.magnetometer = adafruit_lsm303dlh_mag.LSM303DLH_Mag(self.i2c)

        self.log.debug("Initializing accelerometer module...")
        self.accelerometer = adafruit_lsm303_accel.LSM303_Accel(self.i2c)

    def getAccelerometer(self):
        return self.accelerometer.acceleration

    def getMagnetometer(self):
        return self.magnetometer.magnetic
