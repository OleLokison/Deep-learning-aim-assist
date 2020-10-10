from threading import Thread, Lock
from time import time, sleep
from ctypes import Structure, windll, c_uint, sizeof, byref
from pynput import mouse, keyboard


for i in range(100):
    windll.user32.mouse_event(0x0001, 2, -5, 0, 0)
    sleep(0.01)