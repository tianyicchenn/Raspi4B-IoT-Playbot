import time

import RPi.GPIO as GPIO


class Laser:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def lase(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def shutdown(self):
        GPIO.output(self.pin, GPIO.LOW)

    def exit(self):
        GPIO.cleanup()

    def loop(self, duration, interval):
        GPIO.output(self.pin, GPIO.HIGH)
        time.sleep(duration)
        GPIO.output(self.pin, GPIO.LOW)
        time.sleep(interval)
