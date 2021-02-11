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

class MouseControlV4(Thread):
    def __init__(self):
        Thread.__init__(self)
        None
    def run(self):
        #32 directions, 512 distances, 1 Iteration = 0.015
        global distx, disty, strength, Exceptions, MaxIterations
        Ldistx, Ldisty = distx, disty
        while StopKey:
            if Ldistx != distx or Ldisty != disty:
                t = time.time()
                Ldistx = distx
                Ldisty = disty
                Lstrength = strength
                LExceptions = Exceptions
                LMaxIterations = MaxIterations
                x = distx*strength
                y = disty*strength
                #print(x,y)
                if x not in Exceptions or y not in Exceptions:
                    if min(x,y)<=1:
                        windll.user32.mouse_event(0x0001, int(x), int(y), 0, 0)
                    else:
                        if min(x,y)>MaxIterations:
                            Iterations = 6
                        else:
                            Iterations=ceil(min(x,y))
                        x1 = floor(x/(Iterations-1))
                        y1 = floor(y/(Iterations-1))
                        for i in range(Iterations-1):
                            windll.user32.mouse_event(0x0001, x1, y1, 0, 0)
                            #time.sleep(0.005)
                        windll.user32.mouse_event(0x0001, int(x)-(x1*Iterations-1), int(y)-(y1*Iterations-1), 0, 0)
                print(time.time()-t)
            time.sleep(0.05)

distx, disty = 0, 0
strength = 0.1
Exceptions = [-76.2, 33.3, -35.699999999999996, 77.0, -88.5, -127.0, -97.5, 32.5, -21.5, -68.0, -254]
MaxIterations = 3
StopKey = True

inst1 = MouseControlV4()
inst1.daemon = True
inst1.start()


distx, disty = 10, 100

time.sleep(1)