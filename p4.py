from threading import Thread
from time import time, sleep
from ctypes import Structure, windll, c_uint, sizeof, byref
from pynput import mouse, keyboard
from math import asin, acos

def MouseControl(Direction, velocity=5):
	#32 Diffrent direction possibilities
	Direction=Direction*15
	x = asin(Direction)*velocity
	y = acos(Direction)*velocity
	if Direction >= 7 and Direction <= 12:
		y=y*-1
	elif Direction >= 13 and Direction <= 18:
		x=x*-1
		y=y*-1
	elif Direction <= 19 and Direction <= 23:
		x=x*-1
	windll.user32.mouse_event(0x0001, x, y, 0, 0)

for i in range(100):
	MouseControl(3)