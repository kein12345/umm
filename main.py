import tkinter as tk
from tkinter import *
import time
import serial.tools.list_ports
# window = tk.Tk()
# window.title("iot project")
# window.attributes('-fullscreen', False)
# screen_width = window.winfo_screenwidth()
# screen_height = window.winfo_screenheight()
# print("Size:", screen_width, screen_height)

try:
    ser = serial.Serial(port="/dev/ttyAMA2",baudrate=9600)
    print("success")
except:
    print("cant not open port")

relay1_ON = [1,6,0,0,0,255,201,138]
relay1_OFF = [1,6,0,0,0,0,137,202]

relay2_ON = [2,6,0,0,0,255,201,185]
relay2_OFF = [2,6,0,0,0,0,137,249]

relay3_ON = [3,6,0,0,0,255,200,104]
relay3_OFF = [3,6,0,0,0,0,136,40]

relay4_ON = [4,6,0,0,0,255,201,223]
relay4_OFF = [4,6,0,0,0,0,137,159]

relay5_ON = [5,6,0,0,0,255,200,14]
relay5_OFF = [5,6,0,0,0,0,136,78]

relay6_ON = [6,6,0,0,0,255,200,61]
relay6_OFF = [6,6,0,0,0,0,136,125]


def setdevice1(state):
    if state == True:
        ser.write(relay1_ON)
    else:
        ser.write(relay1_OFF)


def setdevice2(state):
    if state == True:
        ser.write(relay2_ON)
    else:
        ser.write(relay2_OFF)


def setdevice3(state):
    if state == True:
        ser.write(relay3_ON)
    else:
        ser.write(relay3_OFF)


def setdevice4(state):
    if state == True:
        ser.write(relay4_ON)
    else:
        ser.write(relay4_OFF)


def setdevice5(state):
    if state == True:
        ser.write(relay5_ON)
    else:
        ser.write(relay5_OFF)


def setdevice6(state):
    if state == True:
        ser.write(relay6_ON)
    else:
        ser.write(relay6_OFF)


while True:
    print("Relay 1 ON")
    ser.write(relay1_ON)
    time.sleep(2)
    print("Relay 1 OFF")
    ser.write(relay1_OFF)
    time.sleep(2)
    print("Relay 2 ON")
    ser.write(relay2_ON)
    time.sleep(2)
    print("Relay 2 OFF")
    ser.write(relay2_OFF)
    time.sleep(2)
    print("Relay 3 ON")
    ser.write(relay3_ON)
    time.sleep(2)
    print("Relay 3 OFF")
    ser.write(relay3_OFF)
    time.sleep(2)
    print("Relay 4 ON")
    ser.write(relay4_ON)
    time.sleep(2)
    print("Relay 4 OFF")
    ser.write(relay4_OFF)
    time.sleep(2)
    print("Relay 5 ON")
    ser.write(relay5_ON)
    time.sleep(2)
    print("Relay 5 OFF")
    ser.write(relay5_OFF)
    time.sleep(2)
    print("Relay 6 ON")
    ser.write(relay6_ON)
    time.sleep(2)
    print("Relay 6 OFF")
    ser.write(relay6_OFF)
    time.sleep(2)


