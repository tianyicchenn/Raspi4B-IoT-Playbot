import time

import RPi.GPIO as GPIO


class Matrix:
    displays = {
        "cat0": ['00111111', '01000010', '10000100', '10000100', '10000100', '10000100', '01000010', '00111111'],
        "cat1": ['00111111', '01111110', '11111100', '11111100', '11111100', '11111100', '01111110', '00111111'],
        "3": ['00000000', '00000000', '01000100', '10000010', '10010010', '10010010', '01101100', '00000000'],
        "2": ['00000000', '00000000', '10000100', '11000010', '10100010', '10010010', '10001100', '00000000'],
        "1": ['00000000', '00000000', '10000000', '10000100', '10000010', '11111110', '10000000', '00000000'],
        "?": ['00000000', '00000000', '00000100', '00000010', '10100010', '00010010', '00001100', '00000000'],
        "bulb": ['00000000', '00011100', '00100010', '11110001', '11001001', '00100010', '00011100', '00000000'],
        "win": ['00000000', '00010100', '00100000', '00100000', '00100000', '00100000', '00010100', '00000000'],
        "tie": ['00000000', '00100100', '00100000', '00100000', '00100000', '00100000', '00100100', '00000000'],
        "lose": ['00000000', '00100100', '00010000', '00010000', '00010000', '00010000', '00100100', '00000000'],
        "error": ['00000000', '01000010', '00100100', '00011000', '00011000', '00100100', '01000010', '00000000'],
        "cloud": ['00010000', '00101000', '00100110', '00100001', '00100001', '00100010', '00100100', '00011000'],
        "sun": ['00010000', '010000100', '00011000', '00100101', '10100100', '00011000', '01000010', '00001000'],
        "clear": ['00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000']
    }

    def __init__(self, ce_pin, din_pin, clk_pin):
        self.din = din_pin
        self.clk = clk_pin
        self.ce = ce_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.din, GPIO.OUT)
        GPIO.setup(self.clk, GPIO.OUT)
        GPIO.setup(self.ce, GPIO.OUT)

    def send(self, byte_data):
        for bit in range(0, 8):
            if (byte_data & 0x80):
                GPIO.output(self.din, True)
            else:
                GPIO.output(self.din, False)
            byte_data = byte_data << 1
            GPIO.output(self.clk, True)
            GPIO.output(self.clk, False)

    def writeWord(self, addr, num):

        #？
        GPIO.output(self.ce, True)
        GPIO.output(self.ce, False)
        GPIO.output(self.clk, False)
        self.send(addr)
        self.send(num)
        GPIO.output(self.ce, True)

    def initData(self):
        self.writeWord(0x09, 0x00)
        self.writeWord(0x0a, 0x03)
        self.writeWord(0x0b, 0x07)
        self.writeWord(0x0c, 0x01)
        self.writeWord(0xff, 0x00)

    def write_matrix(self, index):
        for i in range(0, 8):
            self.writeWord(i + 1, int(self.displays[index][i], 2))

    def clear(self):
        for i in range(0, 8):
            self.writeWord(i + 1, int(self.displays["clear"][i], 2))

    def display(self, image, duration, interval):
        self.initData()
        self.write_matrix(image)
        time.sleep(duration)
        self.clear()
        time.sleep(interval)

    def hold(self, image):
        self.initData()
        self.write_matrix(image)

    def exit(self):
        self.clear()
        GPIO.cleanup()


'''
matrix = Matrix(8, 10, 11)
try:
    while True:
        matrix.display("win", 1, 0.5)
        matrix.display("tie", 1, 0.5)
        matrix.display("lose", 1, 0.5)
        matrix.display("error", 1, 0.5)
        for i in range(3):
            matrix.display("bulb", 0.5, 0.5)
        for i in range(5):
            matrix.display("?", 0.5, 0.1)

        for i in range(3):
            matrix.display("cat0", 1, 0.5)
        for i in range(3):
            matrix.display("cat1", 1, 0.5)
except KeyboardInterrupt:
    matrix.exit()

'''
