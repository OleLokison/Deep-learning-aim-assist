from PIL import Image as Pil_image, ImageTk as Pil_imageTk
import pyautogui
from time import time, sleep
from pynput import keyboard
from threading import Thread
from time import time, sleep, gmtime, strftime
#from ctypes import Structure, windll, c_uint, sizeof, byref
from pynput import mouse, keyboard
from win32gui import FindWindow, SetForegroundWindow, GetClientRect, ClientToScreen
from os import walk
from tkinter import *

FilePath = r"D:\K14\Dataset\Prototyp\\"

def FileNameFinder():
	#seraches in directory for latest count and adapts the count variable
	global count, FilePath, FileNames
	AllNames=[]
	for (dirpath, dirnames, filenames) in walk(FilePath):
		for filename in filenames:
			if "2020" in filename:
				AllNames.append(filename)
	return AllNames


def Cropper(Path, x, y):
	image = Pil_image.open(Path)
	width, height = image.size

	TopLeftx, TopLefty 			= (width-x)/2, (height-y)/2
	BottomRightx, BottomRighty 	= (width-x)/2+x, (height-y)/2+y

	im_crop = image.crop((TopLeftx, TopLefty, BottomRightx, BottomRighty))
	return im_crop

class Window(Frame):
    def __init__(self, master=None, image=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        
        load = image
        render = Pil_imageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.pack()

AllNames=FileNameFinder()
FileName = FilePath+AllNames[0]

root = Tk()
app = Window(root, Cropper(FileName, 572, 572))
root.wm_title("Tkinter window")
root.geometry("2560x1440")
root.mainloop()
