import bme680

# Sensor configuration

try:
    sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except (RuntimeError, IOError):
    sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

print("INFO: Calibration data:")
for name in dir(sensor.calibration_data):
    if not name.startswith("_"):
        value = getattr(sensor.calibration_data, name)
        if isinstance(value, int):
            print(f"{name}: {value}")

sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)
sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)

print("INFO: Initial reading:")
for name in dir(sensor.data):
    value = getattr(sensor.data, name)

    if not name.startswith("_"):
        print(f"{name}: {value}")

sensor.set_gas_heater_temperature(320)
sensor.set_gas_heater_duration(150)
sensor.select_gas_heater_profile(0)

def getTemp():
    sensor.get_sensor_data()
    return sensor.data.temperature

def getHumdity():
    sensor.get_sensor_data()
    return sensor.data.humidity

def getPressure():
    sensor.get_sensor_data()
    return sensor.data.pressure

def getGas():
    sensor.get_sensor_data()
    if sensor.data.heat_stable: # Probably should remove this
        sensor.data.gas_resistance
        return sensor.data.gas_resistance
    else:
        print("WARNING: Sensor not heat stable!")
        return None

# Test section do not touch!
def test():
    print("TESTS: Testing humidity, pressure and temp readings.")
    try:
        print(getTemp())
        print("TESTS: Humidity OK.")
    except:
        print("TESTS: Humidity ERROR.")
    try:
        print(getHumdity())
        print("TESTS: Temp OK.")
    except:
        print("TESTS: Temp ERROR.")
    try:
        print(getPressure())
        print("TESTS: Pressure OK.")
    except:
        print("TESTS: Pressure ERROR.")
    try:
        print(getGas())
        print("TESTS: Gas OK.")
    except:
        print("TESTS: Gas ERROR.")