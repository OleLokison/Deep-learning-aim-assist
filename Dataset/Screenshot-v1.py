import pyautogui
from time import time, sleep
from pynput import keyboard
from threading import Thread
from time import time, sleep, gmtime, strftime
#from ctypes import Structure, windll, c_uint, sizeof, byref
from pynput import mouse, keyboard
from win32gui import FindWindow, SetForegroundWindow, GetClientRect, ClientToScreen
from os import walk
Hotkey, StopKey, TriggerKey=False, True, False
#FileRaw = r"D:\K14\Dataset\Raw\\"
FileRaw = r"D:\K14\Dataset\Prototyp\\"
#FileRaw = r"C:\Users\8holz\Desktop\Dataset_prot\\"
#WindowClassName = "Rainbow six siege"
WindowClassName = 'Rainbow Six'
images=[]
count=0
st=None
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
	#seraches in directory for latest count and adapts the count variable
	global count, FileRaw
	for (dirpath, dirnames, filenames) in walk(FileRaw):
		for filename in filenames:
			if strftime("%Y-%m-%d", gmtime()) in filename:
				if len(filename)==16:
					if int(filename[len(filename)-5])+1 > count:
						count = int(filename[len(filename)-5])+1
						print("count changed to:"+str(count))
						print("16--------"+filename)
				elif len(filename)==17:
					if int(filename[len(filename)-6]+filename[len(filename)-5])+1 > count:
						count = int(filename[len(filename)-6]+filename[len(filename)-5])+1
						print("count changed to:"+str(count))
						print("17--------"+filename)
				elif len(filename)==18:
					if int(filename[len(filename)-7]+filename[len(filename)-6]+filename[len(filename)-5])+1 > count:
						count = int(filename[len(filename)-7]+filename[len(filename)-6]+filename[len(filename)-5])+1
						print("count changed to:"+str(count))
						print("18--------"+filename)
		break

def screenshot(window_title=None, factorx=0, factory=0):
    if window_title:
        hwnd = FindWindow(None, window_title)
        if hwnd:
            SetForegroundWindow(hwnd)
            x, y, x1, y1 = GetClientRect(hwnd)
            x, y = ClientToScreen(hwnd, (x, y))
            x1, y1 = ClientToScreen(hwnd, (x1 - x, y1 - y))
            #x,y,x1,y1 position und Grösse
            print(x1*factorx, x1*factory)
            x += int((x1*factorx/2)); x1 -=int((x1*factorx))
            y += int((y1*factory/2)); y1 -= int((y1*factory))
            im = pyautogui.screenshot(region=(x, y, x1, y1))
            return im
        else:
            print('Window not found!')
    else:
        im = pyautogui.screenshot()
        return im

from threading import Thread
from time import time, sleep
from ctypes import Structure, windll, c_uint, sizeof, byref
from pynput import mouse, keyboard
Hotkey, TriggerKey, TriggerSupportKey, TriggerSupportShutDown=False, True, False, True

def TriggerSupport():
    global TriggerKey, TriggerSupportKey, TriggerSupportShutDown
    while TriggerSupportShutDown:
        if TriggerSupportKey:
            TriggerKey=False
            for i in range(2):
                print("Woooooooow")
                sleep(0.1)
                windll.user32.mouse_event(0x0002, 0, 0, 0, 0)
                sleep(0.01)
                windll.user32.mouse_event(0x0004, 0, 0, 0, 0)
            TriggerKey=True
            TriggerSupportKey=False
        sleep(0.005)

def on_press(key):
    global Hotkey
    print(str(key))
    try:
        if key.char=="5":
            KeyboardListener.stop()
        if key.char=="6":
            Hotkey=not(Hotkey)
    except AttributeError:
        None

def on_click(a1,a2,a3,a4):
    print("click")
    global Hotkey, TriggerKey, TriggerSupportKey
    if Hotkey and TriggerKey and a4 and str(a3)=="Button.left":
        TriggerSupportKey=True

TriggerSupportThread = Thread(target=TriggerSupport, daemon=True)
TriggerSupportThread.start()

MouseListener = mouse.Listener(on_click=on_click)
MouseListener.start()

with keyboard.Listener(on_press=on_press) as KeyboardListener:
    KeyboardListener.join()

