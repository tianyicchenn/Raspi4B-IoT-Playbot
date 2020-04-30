import time

from components import Buzzer, Laser, Arm, Matrix
from functions import petCatsDetection


def main():
    option = petCatsDetection.main()
    print(option)
    matrix = Matrix(8, 10, 11)
    if option == "shorthair":
        laser = Laser(18)
        arm = Arm(13)
        for i in range(5):
            matrix.write_matrix("cat1")
            laser.lase()
            arm.move()
    elif option == "persian":
        buzzer = Buzzer(5)
        for i in range(5):
            matrix.write_matrix("cat0")
            buzzer.work(0.5)
            time.sleep(0.2)
    else:
        for i in range(5):
            matrix.display("error", 0.5, 0.5)
        return "None"
    matrix.write_matrix("clear")


if __name__ == "__main__":
    main()
