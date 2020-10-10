from threading import Thread
from time import time, sleep
from ctypes import Structure, windll, c_uint, sizeof, byref
from pynput import mouse, keyboard
from math import sin, cos, radians

def MouseControl(Direction, velocity=5):
	#32 Diffrent direction possibilities
	Direction=radians(Direction*15)
	x = int(sin(Direction)*velocity)
	y = int(cos(Direction)*velocity)*-1
	windll.user32.mouse_event(0x0001, x, y, 0, 0)

"""
#windll.user32.mouse_event(0x0002, 0, 0, 0, 0)
for i in range(100):
	MouseControl(0)
	sleep(0.01)
#windll.user32.mouse_event(0x0004, 0, 0, 0, 0)
"""