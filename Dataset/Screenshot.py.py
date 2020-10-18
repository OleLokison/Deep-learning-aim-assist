import pyautogui
from time import time, sleep
from pynput import keyboard

FileRaw = r"D:\K14\Dataset\Raw"

def screenshot(window_title=None, factor=None):
    if window_title:
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd:
            win32gui.SetForegroundWindow(hwnd)
            x, y, x1, y1 = win32gui.GetClientRect(hwnd)
            x, y = win32gui.ClientToScreen(hwnd, (x, y))
            x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
            im = pyautogui.screenshot(region=(x, y, x1, y1))
            return im
        else:
            print('Window not found!')
    else:
        im = pyautogui.screenshot()
        return im

def key_press(key):
    print(1)

with keyboard(key_press=key_press) as MouseListener:
    MouseListener.start()

aleep(1)