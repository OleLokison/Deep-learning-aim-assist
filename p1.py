from threading import Thread
from time import time, sleep, gmtime, strftime
#from ctypes import Structure, windll, c_uint, sizeof, byref
from pynput import mouse, keyboard
from win32gui import FindWindow, SetForegroundWindow, GetClientRect, ClientToScreen
from os import walk
Hotkey, StopKey=False, True
FileRaw = r"D:\K14\Dataset\Raw\\"
count=0
#trftime("%Y-%m-%d", gmtime())

for (dirpath, dirnames, filenames) in walk(FileRaw):
    for filename in filenames:
        if strftime("%Y-%m-%d", gmtime()) in filename:
            if int(filename[len(filename)-5])+1 > count:
                count = int(filename[len(filename)-5])+1
                print("count changed to:"+str(count))
    break