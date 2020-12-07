from time import time, sleep
from threading import Thread
from time import time, sleep, gmtime, strftime
# from ctypes import Structure, windll, c_uint, sizeof, byref
from win32gui import FindWindow, SetForegroundWindow, GetClientRect, ClientToScreen
import os
import win32api
import tkinter as tk 
import random
import pickle
import tkinter as tk
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
import cv2
import numpy as np

def ImCompareGray(Im1, Im2, FigSize=(10,10)):
    f = plt.figure(figsize=FigSize)
    f.add_subplot(1,2, 1)
    plt.imshow(Im1, cmap="gray")
    f.add_subplot(1,2, 2)
    plt.imshow(Im2, cmap="gray")
    plt.show(block=True)


DATADIR1 = r"D:\K14\Dataset\K14-Dataset-0-Multi-V1.pickle"
DATADIR2 = r"D:\K14\Dataset\572x572\\"
DATADIR0 = r"D:\K14\Dataset\K14-Dataset-0-Stuff"
ImageTesten=None
PredImage=pickle.load(open(DATADIR0, "rb"))[1][0]
Images = pickle.load(open(DATADIR0, "rb"))[1]
#img = tk.PhotoImage(file=DATADIR2+os.listdir(DATADIR2)[0])



class myThread(Thread):
	def __init__(self):
		Thread.__init__(self)
		None
	def run(self):
		# saves the images in the global list
		root = tk.Tk()
		canvas = tk.Canvas(root, width = 512, height = 512)
		canvas.pack()
		def recursive():
			global ImageTesten, PredImage
			ImageTesten = ImageTk.PhotoImage(Image.fromarray((cv2.cvtColor(PredImage,cv2.COLOR_GRAY2RGB) * 255).astype(np.uint8)))
			#ImageTesten = tk.PhotoImage(file=DATADIR2+random.choice(os.listdir(DATADIR2)))
			canvas.create_image(0,0, anchor=tk.NW, image=ImageTesten)
			root.after(100, recursive)
		recursive()
		root.mainloop()

inst = myThread()
inst.start()

t = time()
while time()-t < 10:
	PredImage = random.choice(Images)