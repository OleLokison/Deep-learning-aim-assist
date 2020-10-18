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
count=0
st=None

for (dirpath, dirnames, filenames) in walk(FileRaw):
    for filename in filenames:
        if strftime("%Y-%m-%d", gmtime()) in filename:
            if int(filename[len(filename)-5])+1 > count:
                count = int(filename[len(filename)-5])+1
                print("count changed to:"+str(count))
    break

def screenshot(window_title=None, factor=None):
    if window_title:
        hwnd = FindWindow(None, window_title)
        if hwnd:
            SetForegroundWindow(hwnd)
            x, y, x1, y1 = GetClientRect(hwnd)
            x, y = ClientToScreen(hwnd, (x, y))
            x1, y1 = ClientToScreen(hwnd, (x1 - x, y1 - y))
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

KeyboardListener = keyboard.Listener(on_press=on_press)
KeyboardListener.start()

while StopKey:
    if Hotkey:
        image = screenshot("Rainbow Six")
        print(time()-st)
        image.save(FileRaw+
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