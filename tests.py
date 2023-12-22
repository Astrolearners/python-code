from .modules.sensors import bme680
from .modules.communication import gps
from .modules.communication import radio
<<<<<<< HEAD
from .modules.helpers import csv_handler
=======
from .modules.helpers import csv_handler, nmea_parser
>>>>>>> 4559cd12a56fd86b54b8e0728a761398ea239eed
from .modules.other import buzzer

print("INFO: Running tests...")

print("TESTS: Communication tests...")

gps.test()
radio.test()

print("TESTS: Running sensor tests...")

bme680.test()

print("TESTS: Running other tests...")

buzzer.test()

print("TESTS: Running helper tests...")

nmea_parser.test()