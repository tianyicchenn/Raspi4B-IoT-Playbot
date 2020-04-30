import RPi.GPIO as GPIO


class SoundSensor:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def status(self):
        return GPIO.input(self.pin)  # LOW when sound detected

    def exit(self):
        GPIO.cleanup()
