import random

from components import Matrix, Arm, Claw, Button
from functions import gestureDetection


def init_robo(claw_pin, arm_pin):
    global claw, arm, matrix
    claw = Claw(claw_pin)
    arm = Arm(arm_pin)


def init_matrix(ce_pin, din_pin, clk_pin):
    global matrix
    matrix = Matrix(ce_pin, din_pin, clk_pin)


def play():
    matrix.write_matrix("3")
    arm.move()
    matrix.write_matrix("2")
    arm.move()
    matrix.write_matrix("1")
    arm.move()
    robo_choice = ["fist", "hand_open", "victory"][random.randint(0, 2)]
    claw.goToPosition(robo_choice)
    human_choice = get_gesture()
    if human_choice not in ["fist", "hand_open", "victory"]:
        for i in range(3):
            matrix.display("error", 1.5, 0.5)
    else:
        result = compare(human_choice, robo_choice)
        for i in range(3):
            matrix.display(result, 1.5, 0.5)


def get_gesture():
    gesture = gestureDetection.main()
    return gesture


def compare(human_choice, robo_choice):
    if human_choice == robo_choice:
        return "tie"
    elif (human_choice, robo_choice) in [("fist", "victory"), ("victory", "hand_open"), ("hand_open", "fist")]:
        return "win"
    else:
        return "lose"


def exit():
    matrix.display("clear", 1, 0)
    matrix.exit()
    claw.exit()


def loop():
    button_r = Button(17)
    while True:
        matrix.display("?", 1, 0.2)


        if not button_r.status():
            break
        else:
            gesture = get_gesture()
            print(gesture)
            if gesture in ("thumb_up"):
                play()
            elif gesture in ("thumb_down"):
                print("end")
                break
    exit()


if __name__ == "__main__":
    init_robo(12, 13)
    init_matrix(8, 10, 11)
    try:
        loop()
    except KeyboardInterrupt:
        exit()
