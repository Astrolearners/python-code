import pigpio
import time

from modules.helpers.logger import logger

class softwareSerial():
    def __init__(self, txd_pin, rxd_pin, baudrate, timeout=15, bol="/r/n", eol="/r/n"):
        self.logger = logger("softwareSerial")

        self.txd = txd_pin
        self.rxd = rxd_pin
        self.baudrate = baudrate
        self.timeout = timeout
        self.bol = bol
        self.eol = eol

        self.logger.info("Initializing pigpio...")
        self.pigpio = pigpio.pi()

        if not self.pigpio.connected:
            self.logger.critical("Pigpio daemon not started! Start with: `sudo pigpiod`. Exiting...")
            exit()

        self.logger.info("Initializing pins...")

        self.pigpio.set_mode(self.txd, pigpio.OUTPUT)
        self.pigpio.set_mode(self.rxd, pigpio.INPUT)

        pigpio.exceptions = False
        self.pigpio.bb_serial_read_close(self.rxd)
        
        pigpio.exceptions = True
        
        self.pigpio.bb_serial_read_open(self.rxd, self.baudrate)

    def write(self, message):
        self.logger.debug("Clearing wave...")
        self.pigpio.wave_clear()
        self.logger.debug("Creating message and connection...")
        self.pigpio.wave_add_serial(self.txd, self.baudrate, str(f"{message}\n").encode())
        self.logger.debug("Creating wave...")
        wave = self.pigpio.wave_create()
        self.logger.debug("Sending data...")
        self.pigpio.wave_send_once(wave)
        while self.pigpio.wave_tx_busy():
            pass
        self.logger.debug("Deleting wave...")
        self.pigpio.wave_delete(wave)

    def read(self):
        try:
            final_string = ""
            start = time.perf_counter()
            while round((time.perf_counter() - start), 2) < self.timeout:
                (byte_count, data) = self.pigpio.bb_serial_read(self.rxd)

                if data:
                    try:
                        data = data.decode("utf-8")
                    except AttributeError:
                        pass

                    final_string = final_string + data

                    if final_string.find(self.bol) != -1:
                        while int(byte_count) > 0:
                            (byte_count, data) = self.pigpio.bb_serial_read(self.rxd)

                            try:
                                data = data.decode("utf-8")
                            except AttributeError:
                                pass

                            final_string = final_string + data

                            if final_string.find(self.eol) != -1:
                                final_string = final_string.strip(self.bol)
                                final_string = final_string.strip(self.eol)
                                return final_string
            self.logger.warning("Timeout reached!")
            return None
        except Exception as e:
            self.logger.error(f"Failed to get data, error: {e}")