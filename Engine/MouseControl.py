from time import time, sleep
from ctypes import windll
from math import sin, cos, radians

def MouseControl(Direction, velocity=5):
	#32 Diffrent direction possibilities
	Direction=radians(Direction*15)
	x = int(sin(Direction)*velocity)
	y = int(cos(Direction)*velocity)*-1
	windll.user32.mouse_event(0x0001, x, y, 0, 0)

def MouseControlT(Direction, distance, velocity=5):
    #32 directions
    #512 distances
    #
    Direction=radians(Direction*15)
    x = int(sin(Direction)*velocity)
    y = int(cos(Direction)*velocity)*-1
    for i in range(int(distance/velocity)):
        windll.user32.mouse_event(0x0001, x, y, 0, 0)
        sleep(0.01)

MouseControlT(12, 512, 10)
"""
for i in range(100):
    t = time()
    MouseControl(6, 5)
    sleep(0.01)
    print(time()-t)
"""