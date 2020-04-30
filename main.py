from components import *
from functions import *
from models import *


def enable_sound():
    sound = SoundSensor(25)
    while True:
        if not sound.status():
            for i in range(2):
                bulb.blink(1, "green", 0.5)
            decide_mode()


def decide_mode():
    if faceDetection.main():
        play_game()
    elif petCatsDetection.main() != "error":
        teaseCats.main()
    else:
        report_error()


def report_error():
    for i in range(3):
        matrix.display("error", 0.5, 0.2)


def play_game():
    matrix.display("bulb", 0.5, 0.2)
    matrix.display("bulb", 0.5, 0.2)
    playRPS.init_robo(12, 13)
    playRPS.init_matrix(8, 10, 11)
    playRPS.loop()


def loop():
    while True:
        if not button_r.status():
            bulb.blink(1, "red", 0.5)
            bulb.blink(1, "red", 0.5)
            enable_sound()
        if not button_b.status():
            bulb.blink(1, "blue", 0.5)
            iotWeather.main()


if __name__ == "__main__":
    button_r = Button(17)
    button_b = Button(27)
    bulb = Bulb(16, 20, 21)
    matrix = Matrix(8, 10, 11)
    try:
        loop()
    except KeyboardInterrupt:
        matrix.clear()
        bulb.exit()

