from gpiozero import Buzzer
from time import sleep

from modules.helpers.logger import logger

class buzzer():
    def __init__(self):
        self.log = logger("buzzer")

        self.log.info("Initializing buzzer...")
        try:
            self.buzzer = Buzzer(21)
        except Exception as e:
            self.log.error(f"Failed to initialize buzzer! Error: {e}")

    def beep(self, delay, times):
        self.log.debug(f"Turning buzzer on and sleeping {delay} second(s) for {times} time(s)...")
        for i in range(times):
            self.buzzer.on()
            sleep(delay)
            self.buzzer.off()

# Tests not ready
# def test():
#     print("TESTS: Bipping buzzer.")
#     try:
#         print(buzz())
#         print("TESTS: Buzzer OK.")
#     except:
#         print("TESTS: Buzzer ERROR.")