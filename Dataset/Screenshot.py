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
"""
def enum_window_titles():
    #returns all open window class names
    def callback(handle, data):
        titles.append(win32gui.GetWindowText(handle))

    titles = []
    win32gui.EnumWindows(callback, None)
    return titles
"""
def FilenameFlow():
    #seraches in directory for latest count and adapts the count variable
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

def Photographer():
    #gets keypress signal(Hotkey), generates and saves Screenshot
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

FilenameFlow()
KeyboardListener = keyboard.Listener(on_press=on_press)
KeyboardListener.start()
Photographer()