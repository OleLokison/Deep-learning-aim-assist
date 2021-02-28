import os
import pickle
from win32gui import FindWindow, SetForegroundWindow, GetClientRect, ClientToScreen
import pyautogui
import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
from matplotlib import pyplot as plt
from ctypes import windll
from math import floor, ceil
import win32api
import time
from threading import Thread

def Coords(Pred, small):
	#cv2, Predicitons.pickle[2]=small
	Pred = (255 - cv2.inRange(np.array(Pred * 255, dtype = np.uint8), 0, 160)).astype(np.float32)
	small = np.array(small * 255, dtype = np.uint8).astype(np.float32)
	result = cv2.matchTemplate(Pred, small, cv2.TM_SQDIFF_NORMED)
	mn,_,mnLoc,_ = cv2.minMaxLoc(result)
	MPx,MPy = mnLoc
	#x and y may flipped
	return (MPx+2-256, MPy+2-256)
	#return (MPx, MPy)

def ImCompareGray(Im1, Im2, FigSize=(10,10)):
    f = plt.figure(figsize=FigSize)
    f.add_subplot(1,2, 1)
    plt.imshow(Im1, "gray")
    f.add_subplot(1,2, 2)
    plt.imshow(Im2)
    plt.show(block=True)

class myThread(Thread):
	def __init__(self):
		Thread.__init__(self)
		None
	def run(self):
		# saves the images in the global list
		root = tk.Tk()
		canvas1 = tk.Canvas(root, width = 512, height = 512)
		canvas1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
		def recursive():
			global ImageTesten0, ImageTesten1, PredImage0, PredImage1
			ImageTesten1 = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(PredImage1, cv2.COLOR_BGR2RGB)))
			#ImageTesten = tk.PhotoImage(file=DATADIR2+random.choice(os.listdir(DATADIR2)))
			canvas1.create_image(0,0, anchor=tk.NW, image=ImageTesten1)
			root.after(100, recursive)
		recursive()
		root.mainloop()

Template = pickle.load(open(r"D:\K14\Dataset\Predicitions.pickle", "rb"))[10]
ims = pickle.load(open(r"D:\K14\Dataset\TestImages.pickle", "rb"))
Cache = pickle.load(open(r"C:\Users\8holz\Dokumente\GitHub\K14\Cache.pickle", "rb"))


i = 8
ImageTesten0, ImageTesten1, PredImage0, PredImage1 = ims[1][i], ims[0][i], ims[1][i], ims[0][i]

inst = myThread()
inst.start()