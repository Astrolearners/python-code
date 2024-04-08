from gpiozero import Buzzer, TonalBuzzer
from time import sleep

from modules.helpers.logger import logger

class buzzer():
    def __init__(self, pin, type="passive"):
        self.log = logger("buzzer")
        self.type = type
        self.pin = pin

        self.log.info("Initializing buzzer...")
        if self.type == "passive":
            self.buzzer = TonalBuzzer(self.pin)
        elif self.type == "active":
            self.buzzer = Buzzer(self.pin)
        else:
            self.log.error("Invalid buzzer type!")

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