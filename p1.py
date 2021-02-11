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
#260, 260
def ImCompareGray(Im1, Im2, FigSize=(10,10)):
    f = plt.figure(figsize=FigSize)
    f.add_subplot(1,2, 1)
    plt.imshow(Im1, "gray")
    f.add_subplot(1,2, 2)
    plt.imshow(Im2)
    plt.show(block=True)

Template = pickle.load(open(r"D:\K14\Dataset\Predicitions.pickle", "rb"))
ims = pickle.load(open(r"D:\K14\Dataset\TestImages.pickle", "rb"))
image = ims[1][8]
image = (255 - cv2.inRange(np.array(image * 255, dtype = np.uint8), 0, 160)).astype(np.float32)


for i in Template:
	print(i.shape)


p = 260
size = 5
t = []

Template = np.array(Template[0] * 255, dtype = np.uint8).astype(np.float32)
for i in range(1, 46):
	ima = image[p:p+size+i, p:p+size+i]
	ima = ima.reshape(size+i, size+i, 1)
	t.append(np.array(ima * 255, dtype = np.uint8).astype(np.float32))
for i in t:
	print(i.shape)


pickle.dump(t, open(r"D:\K14\Dataset\Predicitions.pickle", "wb"))

"""
war beim erstellen von neuen Templates, richtig frustrierend das richtige format zu bekommen
"""