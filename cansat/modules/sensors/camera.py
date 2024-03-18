from picamera2 import Picamera2
import datetime

from modules.helpers.logger import logger

class camera():
    def __init__(self, capture_path):
        self.log = logger("camera")
        self.capture_path = capture_path

        self.log.debug("Configuring camera")
        self.picam2 = Picamera2()
        self.config = self.picam2.create_still_configuration()
        self.picam2.configure(self.config)

    def start(self):
        self.log.debug("Starting camera")
        self.picam2.start()

    def stop(self):
        self.log.debug("Stopping camera")
        self.picam2.stop()

    def capture(self):
        date_time = datetime.datetime.now()
        file_name = date_time.strftime("%d_%m_%y-%H-%M-%S.jpg")
        self.log.info("Capturing image")
        self.picam2.capture_file(f"{self.capture_path}/{file_name}")