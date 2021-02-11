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

Template = pickle.load(open(r"D:\K14\Dataset\Predicitions.pickle", "rb"))[3]
ims = pickle.load(open(r"D:\K14\Dataset\TestImages.pickle", "rb"))

i = 8

print(Template.shape)

c = Coords(ims[1][i], Template)
print(c)
print(c[0]+256, c[1]+256)

image = cv2.rectangle(ims[0][i], (c[0]+256, c[1]+256), (c[0]+256+2, c[1]+256+2), (0,255,0), 2)
"""
cv2.imshow("image", image)
cv2.waitKey()
"""

ImCompareGray(ims[1][i], image)
