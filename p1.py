from time import time, sleep
from threading import Thread
from time import time, sleep, gmtime, strftime
# from ctypes import Structure, windll, c_uint, sizeof, byref
from win32gui import FindWindow, SetForegroundWindow, GetClientRect, ClientToScreen
from os import walk
import win32api
import tkinter as tk 
import random
import pickle

PredImage=None
DATADIR2 = r"D:\K14\Dataset\K14-Dataset-0-Multi-V1.pickle"

def Prep(tim, pause):
	global PredImage
	t1 = time()
	#Images = pickle.load(open(DATADIR2), "rb")["TestImages0"]
	Images = [1,2,3,4,5,6,7,8,9]
	while (time()-t1<=tim):
		PredImage = random.choice(Images)
		sleep(pause)
		#print(PredImage)

class myThread(Thread):
	def __init__(self):
		Thread.__init__(self)
		None
	def run(self):
		# saves the images in the global list
		root = tk.Tk()

		def refresh():
			global PredImage
			print(PredImage)
			root.after(1000, refresh)
		refresh()
		root.mainloop()

inst = myThread()
inst.start()
Prep(5, 0.5)