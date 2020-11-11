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

state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128

"""
from win32gui import GetWindowText, EnumWindows
def enum_window_titles():
	#returns all open window class names
	def callback(handle, data):
		titles.append(GetWindowText(handle))
	titles = []
	EnumWindows(callback, None)
	return titles
print(enum_window_titles())
"""


def FilenameFlow():
	# seraches in directory for latest count and adapts the count variable
	global count, FileRaw
	for (dirpath, dirnames, filenames) in walk(FileRaw):
		for filename in filenames:
			if strftime("%Y-%m-%d", gmtime()) in filename:
				if len(filename) == 16:
					if int(filename[len(filename) - 5]) + 1 > count:
						count = int(filename[len(filename) - 5]) + 1
						print("count changed to:" + str(count))
						print("16--------" + filename)
				elif len(filename) == 17:
					if int(filename[len(filename) - 6] + filename[len(filename) - 5]) + 1 > count:
						count = int(filename[len(filename) - 6] + filename[len(filename) - 5]) + 1
						print("count changed to:" + str(count))
						print("17--------" + filename)
				elif len(filename) == 18:
					if int(filename[len(filename) - 7] + filename[len(filename) - 6] + filename[
						len(filename) - 5]) + 1 > count:
						count = int(
							filename[len(filename) - 7] + filename[len(filename) - 6] + filename[len(filename) - 5]) + 1
						print("count changed to:" + str(count))
						print("18--------" + filename)
		break

"""
def screenshot(window_title=None, factorx=0, factory=0):
	if window_title:
		hwnd = FindWindow(None, window_title)
		if hwnd:
			SetForegroundWindow(hwnd)
			x, y, x1, y1 = GetClientRect(hwnd)
			x, y = ClientToScreen(hwnd, (x, y))
			x1, y1 = ClientToScreen(hwnd, (x1 - x, y1 - y))
			# x,y,x1,y1 position and size
			print(x1 * factorx, x1 * factory)
			x += int((x1 * factorx / 2));
			x1 -= int((x1 * factorx))
			y += int((y1 * factory / 2));
			y1 -= int((y1 * factory))
			im = pyautogui.screenshot(region=(x, y, x1, y1))
			return im
		else:
			print('Window not found!')
	else:
		im = pyautogui.screenshot()
		return im
"""
def screenshot(window_title=None, factorx=0, factory=0):
	print("SCREENSHOT IS MADE")


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


class myThread(Thread):
	def __init__(self):
		Thread.__init__(self)
		None

	def run(self):
		# saves the images in the global list
		print(4)
		global StopKey, images, FileRaw, count
		while StopKey:
			if len(images) > 0:
				images[0].save(FileRaw +
				               strftime("%Y-%m-%d", gmtime()) +
				               "-" +
				               str(count) +
				               ".png")
				print(FileRaw +
				      strftime("%Y-%m-%d", gmtime()) +
				      "-" +
				      str(count) +
				      ".png")
				images.pop(0)
				count += 1
			sleep(0.05)


def Photographer():
	# gets keypress signal(Hotkey), generates and appends screenshot to global list
	global StopKey, Hotkey, images, count, FileRaw, FileRaw, WindowClassName, state_left, state_right
	while StopKey:

		if Hotkey:
			images.append(screenshot(WindowClassName))
			Hotkey = False

		b = win32api.GetKeyState(0x02)

		if b != state_right:  # Button state changed
			state_right = b
			i = 0
			
			if b < 0:
				print('Right Button Pressed')
				start = time()
				while (b == state_right):
					b = win32api.GetKeyState(0x02)
					i+=1
					images.append(screenshot(WindowClassName))
					print('screenshot {}'.format(i))
					sleep(0.25)
					end = time()
					if end-start > 4:
						print("4 seconds delay")
						break
			else:
				print('Right Button Released')

FilenameFlow()

KeyboardListener = keyboard.Listener(on_press=on_press)
KeyboardListener.start()

"""
saveimages = myThread()
saveimages.start()
"""

 
Photographer()