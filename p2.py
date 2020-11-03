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
	if Hotkey and TriggerKey and a4:
		TriggerSupportKey=True

TriggerSupportThread = Thread(target=TriggerSupport, daemon=True)
TriggerSupportThread.start()

MouseListener = mouse.Listener(on_click=on_click)
MouseListener.start()

with keyboard.Listener(on_press=on_press) as KeyboardListener:
	KeyboardListener.join()

"""
will detecten, kann aber nicht weil funktion schon gecallt
"""