from win32gui import FindWindow, SetForegroundWindow, GetClientRect, ClientToScreen
import pyautogui
from time import sleep

WindowClassName = 'Rainbow Six'

def screenshot(window_title=None, factorx=0, factory=0):
	if window_title:
		hwnd = FindWindow(None, window_title)
		if hwnd:
			SetForegroundWindow(hwnd)
			x, y, x1, y1 = GetClientRect(hwnd)
			x, y = ClientToScreen(hwnd, (x, y))
			x1, y1 = ClientToScreen(hwnd, (x1 - x, y1 - y))
			# x,y,x1,y1 position and size
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
sleep(10)

while True:
    screenshot(WindowClassName)
    sleep(0.1)