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
moment = False
beginstate = win32api.GetKeyState(0x01)
timepoint = None
Hotkey, StopKey = False, True
FileRaw = r"D:\K14\Dataset\Raw\\"
# FileRaw = r"C:\Users\8holz\Desktop\Dataset_prot\\"
# WindowClassName = "Rainbow six siege"
WindowClassName = 'Rainbow Six'
images = []
count = 0
st = None

def on_press(key):
	global Hotkey, StopKey, st
	print(str(key))
	try:
		if key.char == "5":
			KeyboardListener.stop()
			StopKey = False
		if key.char == "q" or key.char == "Q":
			Hotkey = True
			st = time()
	except AttributeError:
		None


def Photographer():
	print("Photographer")
	# if Mouse is clicked provisional to final
	global StopKey
	beginstate = win32api.GetKeyState(0x01)
	print(beginstate)
	moment = 1
	while StopKey:
		MouseState = win32api.GetKeyState(0x01)
		if MouseState == -127 or MouseState == -128:  # Button state changed
			moment =time()
		else:
			print(time()-moment)5
		sleep(0.001)

KeyboardListener = keyboard.Listener(on_press=on_press)
KeyboardListener.start()

Photographer()