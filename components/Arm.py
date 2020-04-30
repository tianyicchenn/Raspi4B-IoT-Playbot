import time

from gpiozero import Servo
import RPi.GPIO as GPIO


class Arm:
    def __init__(self, pin):
        self.pin = pin
        self.arm = Servo(self.pin)
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.OUT)

    def move(self):
        self.arm.max()
        time.sleep(0.8)
        self.arm.mid()
        time.sleep(0.8)