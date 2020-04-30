# coding=utf-8
import os
import time

from components import Bulb, Humidifier, Matrix
from functions import getWeather, aliyunConnect


def display_weather():
    matrix = Matrix(8, 10, 11)
    weather = getWeather.main()
    if weather == "晴":
        wea = 0
        for i in range(3):
            matrix.display("sun", 0.5, 0.2)
    else:
        wea = 1
        for i in range(3):
            matrix.display("cloud", 0.5, 0.2)
    connect(wea)


def connect(weather_data):
    os.system("sudo python3 /home/pi/Desktop/code/run.py")
    aliyunConnect.main(weather_data, 0)


def get_humi():
    bulb = Bulb(16, 20, 21)
    for i in range(3):
        bulb.blink(0.5, "yellow", 0.2)
    humidifier = Humidifier(24)
    humidifier.work(15)


def main():
    display_weather()
    time.sleep(5)
    get_humi()
