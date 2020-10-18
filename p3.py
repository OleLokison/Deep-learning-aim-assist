import pyautogui
from time import time, sleep
from win32gui import FindWindow, SetForegroundWindow, GetClientRect, ClientToScreen

def screenshot(window_title=None):
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

sleep(0)
st = time()
im = screenshot('Rainbow six')
print(time()-st)
