import bme680
from modules.helpers.logger import logger

class bme():
    def __init__(self):
        self.log = logger("bme680")

        try:
            self.sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
        except (RuntimeError, IOError):
            self.sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

        self.log.info("Calibration data:")
        for name in dir(self.sensor.calibration_data):
            if not name.startswith("_"):
                value = getattr(self.sensor.calibration_data, name)
                if isinstance(value, int):
                    print(f"{name}: {value}")

        self.log.info("Setting sensor configuration...")
        self.sensor.set_humidity_oversample(bme680.OS_2X)
        self.sensor.set_pressure_oversample(bme680.OS_4X)
        self.sensor.set_temperature_oversample(bme680.OS_8X)
        self.sensor.set_filter(bme680.FILTER_SIZE_3)
        self.sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)

        self.log.debug("Initial reading:")
        for name in dir(self.sensor.data):
            value = getattr(self.sensor.data, name)

            if not name.startswith("_"):
                print(f"{name}: {value}")

        self.sensor.set_gas_heater_temperature(320)
        self.sensor.set_gas_heater_duration(150)
        self.sensor.select_gas_heater_profile(0)

    def getTemp(self):
        self.sensor.get_sensor_data()
        return self.data.temperature

    def getHumidity(self):
        self.sensor.get_sensor_data()
        return self.sensor.data.humidity

    def getPressure(self):
        self.sensor.get_sensor_data()
        return self.sensor.data.pressure

    def getGas(self):
        self.sensor.get_sensor_data()
        if self.sensor.data.heat_stable:
            self.sensor.data.gas_resistance
            return self.sensor.data.gas_resistance
        else:
            self.log.warn("Sensor not heat stable!")
            return None

# Test section do not touch! Not ready
# def test():
#     print("TESTS: Testing humidity, pressure and temp readings.")
#     try:
#         print(getTemp())
#         print("TESTS: Humidity OK.")
#     except:
#         print("TESTS: Humidity ERROR.")
#     try:
#         print(getHumdity())
#         print("TESTS: Temp OK.")
#     except:
#         print("TESTS: Temp ERROR.")
#     try:
#         print(getPressure())
#         print("TESTS: Pressure OK.")
#     except:
#         print("TESTS: Pressure ERROR.")
#     try:
#         print(getGas())
#         print("TESTS: Gas OK.")
#     except:
#         print("TESTS: Gas ERROR.")