from modules.sensors import adxl335, bme680
from modules.communication import gps, radio
# from modules.helpers import 
from modules.other import buzzer

print("INFO: Running tests...")

print("INFO: Communication tests...")

gps.test()
radio.test()

print("INFO: Running sensor tests...")

adxl335.test()
bme680.test()

print("INFO: Running other tests...")

buzzer.test()

print("INFO: Running helper tests...")

# Nothing here