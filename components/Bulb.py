import time

import RPi.GPIO as GPIO


class Bulb:
    colorSet = {
        "red": (100, 0, 0),
        "green": (0, 100, 0),
        "blue": (0, 0, 100),
        "yellow": (100, 100, 0),
        "magenta": (100, 0, 100),
        "cyan": (0, 100, 100),
        "white": (100, 100, 100)
    }

    def __init__(self, pinR, pinG, pinB):
        self.pinR = pinR
        self.pinG = pinG
        self.pinB = pinB
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pinR, GPIO.OUT)
        GPIO.setup(self.pinG, GPIO.OUT)
        GPIO.setup(self.pinB, GPIO.OUT)
        global pwmR, pwmG, pwmB
        pwmR = GPIO.PWM(self.pinR, 60)
        pwmG = GPIO.PWM(self.pinG, 60)
        pwmB = GPIO.PWM(self.pinB, 60)

    def blink(self, duration, color, interval):
        rValue, gValue, bValue = self.colorSet[color]
        pwmR.start(0)
        pwmG.start(0)
        pwmB.start(0)
        pwmR.ChangeDutyCycle(rValue)
        pwmG.ChangeDutyCycle(gValue)
        pwmB.ChangeDutyCycle(bValue)
        time.sleep(duration)
        pwmR.stop()
        pwmG.stop()
        pwmB.stop()
        time.sleep(interval)

    def exit(self):
        pwmR.stop()
        pwmG.stop()
        pwmB.stop()
        GPIO.cleanup()
