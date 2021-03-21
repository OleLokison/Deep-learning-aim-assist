#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
import os
import random
import numpy as np
import matplotlib.pyplot as plt
import pickle
import time
print(tf.version.VERSION)

from win32gui import FindWindow, SetForegroundWindow, GetClientRect, ClientToScreen
import pyautogui
import cv2

import tkinter as tk
from PIL import Image, ImageTk

from threading import Thread


# In[2]:


"""
from win32gui import GetWindowText, EnumWindows
def enum_window_titles():
	#returns all open window class names
	def callback(handle, data):
		titles.append(GetWindowText(handle))
	titles = []
	EnumWindows(callback, None)
	return titles
print(enum_window_titles())
enum_window_titles()
"""


# In[2]:


checkpoint_path = "C:/Users/8holz/Dokumente/GitHub/K14/Training_Protocol/Model-Color-UNET/weights/saved_model.pb"
checkpoint_dir = os.path.dirname(checkpoint_path)

WindowClassName0 = 'Rainbow Six'
WindowClassName1 = 'J2 - Jupyter Notebook - Google Chrome'

PredImage = None


# In[3]:


def screenshot(window_title=None, lenx=512, leny=512):
	if window_title:
		hwnd = FindWindow(None, window_title)
		if hwnd:
			SetForegroundWindow(hwnd)
			x, y, x1, y1 = GetClientRect(hwnd)
			x, y = ClientToScreen(hwnd, (x, y))
			x1, y1 = ClientToScreen(hwnd, (x1 - x, y1 - y))
			# x,y,x1,y1 position and size
			x += int((x1-lenx)/2)
			x1 = lenx
			y += int((y1-leny)/2)
			y1 = leny
			im = pyautogui.screenshot(region=(x, y, x1, y1))
			gray = np.array(im)
			image = np.array(gray).reshape(-1, lenx, leny, 3)
			return image
		else:
			print('Window not found!')
	else:
		im = pyautogui.screenshot()
		gray = cv2.cvtColor(np.array(im))
		image = np.array(gray).reshape(-1, lenx, leny, 3)
		return image


# In[4]:


def load_K14():
    #model = create_model(IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS)
    #model.summary()
    model = tf.keras.models.load_model(checkpoint_dir)
    #model.summary()

    configproto = tf.compat.v1.ConfigProto() 
    configproto.gpu_options.allow_growth = True
    sess = tf.compat.v1.Session(config=configproto) 
    tf.compat.v1.keras.backend.set_session(sess)
    return model


# In[5]:


model = load_K14(
)


# In[6]:


def xyz(image):
    a = time.time()
    im_preds = model.predict(image, verbose=1)
    print(time.time()-a)
    image = image.reshape(512, 512, 3)
    im_preds = im_preds.reshape(512, 512, 1)
    #ImCompareGray(image, im_preds)
    return im_preds


# In[7]:


PredImage=xyz(screenshot(WindowClassName1))


# In[8]:


print(PredImage.shape)
PredImage = PredImage.reshape(-1, 512, 512, 1)


# In[9]:


ImageTesten = None
#ImageTesten = ImageTk.PhotoImage(Image.fromarray((cv2.cvtColor(PredImage,cv2.COLOR_GRAY2RGB) * 255).astype(np.uint8)))


# In[10]:


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


# In[11]:


inst = myThread()
inst.start()


# In[12]:


time.sleep(10)


# In[13]:


while True:
    PredImage=xyz(screenshot(WindowClassName0))
    time.sleep(0.1)


# In[ ]:




