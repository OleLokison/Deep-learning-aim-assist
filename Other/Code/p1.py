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

dir1 = r"D:\K14\Dataset\K14-Dataset-0-Multi-V2.pickle"

a = pickle.load(open(dir1, "rb"))

print(len(a["TrainImages0"]))