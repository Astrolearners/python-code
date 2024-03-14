from gpiozero import Buzzer, TonalBuzzer
from time import sleep

from modules.helpers.logger import logger

class buzzer():
    def __init__(self, type="passive"):
        self.log = logger("buzzer")
        self.type = type

        self.log.info("Initializing buzzer...")
        try:
            if self.type == "passive":
                self.buzzer = TonalBuzzer(21)
            elif self.type == "active":
                self.buzzer = Buzzer(21)
            else:
                self.log.error("Invalid buzzer type!")
        except Exception as e:
            self.log.error(f"Failed to initialize buzzer! Error: {e}")

    def beep(self, delay, times):
        self.log.debug(f"Turning buzzer on and sleeping {delay} second(s) for {times} time(s)...")
        for i in range(times):
            if self.type == "passive":
                self.buzzer.play(self.buzzer.max_tone)
            elif self.type == "active":
                self.buzzer.on()
            else:
                self.log.error("Invalid buzzer type!")
            sleep(delay)
            if self.type == "passive":
                self.buzzer.stop()
            elif self.type == "active":
                self.buzzer.off()
            else:
                self.log.error("Invalid buzzer type!")