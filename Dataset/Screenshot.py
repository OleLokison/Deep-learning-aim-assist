import pyautogui
from time import time, sleep
from pynput import keyboard
from threading import Thread
from time import time, sleep, gmtime, strftime
#from ctypes import Structure, windll, c_uint, sizeof, byref
from pynput import mouse, keyboard
from win32gui import FindWindow, SetForegroundWindow, GetClientRect, ClientToScreen
from os import walk
Hotkey, StopKey=False, True
FileRaw = r"D:\K14\Dataset\Raw\\"
images=[]
count=0
st=None

for (dirpath, dirnames, filenames) in walk(FileRaw):
    for filename in filenames:
        if strftime("%Y-%m-%d", gmtime()) in filename:
            if int(filename[len(filename)-5])+1 > count:
                count = int(filename[len(filename)-5])+1
                print("count changed to:"+str(count))
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

def on_press(key):
    global Hotkey, StopKey, st
    print(str(key))
    try:
        if key.char=="5":
            KeyboardListener.stop()
            StopKey=False
        if key.char=="q":
            Hotkey=True
            st = time()
    except AttributeError:
        None
class myThread(Thread):
	def __init__(self):
		Thread.__init__(self)
		None
	def run(self):
		print(4)
		global StopKey, images
		while StopKey:
			if len(images)>0:
				images[0].save(FileRaw+
					strftime("%Y-%m-%d", gmtime())+
					"-"+
					str(count)+
					".png")
				print(FileRaw+
					strftime("%Y-%m-%d", gmtime())+
					"-"+
					str(count)+
					".png")
				images.pop(0)


KeyboardListener = keyboard.Listener(on_press=on_press)
KeyboardListener.start()

#saveimages = myThread()
#saveimages.start()
while StopKey:
	if Hotkey:
		images


		.append(screenshot("Rainbow Six"))
		print(time()-st)
		images[0].save(FileRaw+
			strftime("%Y-%m-%d", gmtime())+
			"-"+
			str(count)+
			".png")
		print(FileRaw+
			strftime("%Y-%m-%d", gmtime())+
			"-"+
			str(count)+
			".png")
		Hotkey=False
		count+=1
	sleep(0.0005)