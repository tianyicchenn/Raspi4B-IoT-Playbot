import time

import RPi.GPIO as GPIO


class Claw:
    gFPWM = 40
    duties = {
        "fist": 4.8,
        "hand_open": 6.5,
        "victory": 5.5
    }

    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.OUT)
        global pwm
        pwm = GPIO.PWM(self.pin, self.gFPWM)

    def reset(self):
        pwm.start(5)
        pwm.ChangeDutyCycle(5)
        time.sleep(0.2)
        pwm.stop()

    def goToPosition(self, position):
        pwm.start(5)
        duty = self.duties[position]
        pwm.ChangeDutyCycle(duty)
        time.sleep(1)
        pwm.stop()

    def exit(self):
        GPIO.cleanup()

