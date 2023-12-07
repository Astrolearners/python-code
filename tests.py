from .modules.sensors import bme680
from .modules.communication import gps
from .modules.communication import radio
from .modules.helpers import csv_handler
from .modules.other import buzzer

print("INFO: Running tests...")

print("INFO: Communication tests...")

gps.test()
radio.test()

print("INFO: Running sensor tests...")

bme680.test()

print("INFO: Running other tests...")

buzzer.test()

print("INFO: Running helper tests...")

# Nothing here