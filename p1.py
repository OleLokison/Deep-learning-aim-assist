import pyautogui
from time import time, sleep
from pynput import keyboard
from threading import Thread
from time import time, sleep, gmtime, strftime
# from ctypes import Structure, windll, c_uint, sizeof, byref
from pynput import mouse, keyboard
from win32gui import FindWindow, SetForegroundWindow, GetClientRect, ClientToScreen
from os import walk
import win32api

Hotkey, StopKey = False, True
FileRaw = r"D:\K14\Dataset\Raw\\"
# FileRaw = r"C:\Users\8holz\Desktop\Dataset_prot\\"
# WindowClassName = "Rainbow six siege"
WindowClassName = 'Rainbow Six'
images = []
count = 0
st = None

def MouseClickCalibrate():
	global state_right, state_left
	Lock = True
	while Lock:
		state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
		state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128
		if state_right == 1 or state_right == 0 and state_left == 0 or state_left == 0:
			Lock = False


def Photographer():
	print("Photographer")
	# if Mouse is clicked provisional to final
	global StopKey, state_right, state_left
	while StopKey:
		MouseState = win32api.GetKeyState(0x01)
		if MouseState == -127 or MouseState == -128:  # Button state changed
#			FinalImages+=ProvisionallyImages
			state_left = MouseState
			print("Mouse changed")
		else:
			print(1)
while True:
	MouseState = win32api.GetKeyState(0x01)
	print(MouseState)
	sleep(0.001)
