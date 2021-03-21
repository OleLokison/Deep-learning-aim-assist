import numpy as np 
import os
import cv2
from matplotlib import pyplot as plt
from PIL import Image as Pil_image, ImageTk as Pil_imageTk
import pickle
import random

DATADIR0 = r"D:\K14\Dataset\TestImages"
DATADIR1 = r"D:\K14\Dataset\TestImages"
DATADIR2 = r"D:\K14\Dataset\TestImages.pickle"

"""
def LoadImg(InputDir0, InputDir1, ImWidth, ImHeight, TestFraction=0.25):
	#takes images by pah, converts to grayscale aray, shuffles, splits
	print("LoadImg is Running")
	Images0 = []
	Images1 = []
	for i in range(len(os.listdir(InputDir0))):
		array = cv2.imread(os.path.join(InputDir0, os.listdir(InputDir0)[i]))
		Images0.append(array)
	for i in range(len(os.listdir(InputDir1))):
		array = cv2.imread(os.path.join(InputDir1, os.listdir(InputDir1)[i]), cv2.IMREAD_GRAYSCALE)
		Images1.append(array)
	print("LoadImg has finished, yeepa\n")
	return [
		Images0, 
		Images1,
		]
"""
def LoadImg(InputDir0, InputDir1, ImWidth, ImHeight, TestFraction=0.25):
	#takes images by pah, converts to grayscale aray, shuffles, splits
	print("LoadImg is Running")
	Images0 = []
	Images1 = []
	for i in range(len(os.listdir(InputDir0))):
		array = cv2.imread(os.path.join(InputDir0, os.listdir(InputDir0)[i]))
		Images0.append(array)
	for i in range(len(os.listdir(InputDir1))):
		array = cv2.imread(os.path.join(InputDir1, os.listdir(InputDir1)[i]), cv2.IMREAD_GRAYSCALE)
		Images1.append(array)
	print("LoadImg has finished, yeepa\n")
	return [
		Images0, 
		Images1,
		]


def MultImg(Images0, Images1, Multiplications, ShapeTuple):
	print("MultImg is running")
	TestImg = random.choice(Images0), random.choice(Images1)
	if (ShapeTuple[0] > TestImg[0].shape[0] or 
		ShapeTuple[0] > TestImg[1].shape[0] or 
		ShapeTuple[1] > TestImg[0].shape[1] or 
		ShapeTuple[1] > TestImg[1].shape[1]):
		print("ShapeTuple is to Big for Operation")
		return
	PosPixels = {}
	NewImages0 = []
	NewImages1 = []
	PosArea = {
		"xmax":TestImg[0].shape[0]-ShapeTuple[0], 
		"ymax":TestImg[0].shape[1]-ShapeTuple[1]}
	for k in range(len(Images1)):
		print("Img number: "+str(k)+" from: "+str((len(Images1))))
		for m in range(Multiplications):
			if m == Multiplications-1:
				x = int(PosArea["xmax"]/2)
				y = int(PosArea["ymax"]/2)
				NewImage1 = (Images1[k][x:x+ShapeTuple[0], y:y+ShapeTuple[1]])
				NewImage0 = (Images0[k][x:x+ShapeTuple[0], y:y+ShapeTuple[1]])
				NewImages1.append(NewImage1)
				NewImages0.append(NewImage0)
			else:
				if len(PosPixels)>0:
					maxx, maxy = random.choice(list(PosPixels.items()))
					minx, miny = maxx - ShapeTuple[0], maxy - ShapeTuple[1]
					if minx < 0:
						minx = 0
					if miny < 0:
						miny = 0
					if maxx >  TestImg[0].shape[0]-ShapeTuple[0]:
						maxx = TestImg[0].shape[0]-ShapeTuple[0]
					if maxy > TestImg[0].shape[1]-ShapeTuple[1]:
						maxy = TestImg[0].shape[1]-ShapeTuple[1]
					x = random.randrange(minx, maxx)
					y = random.randrange(miny, maxy)
					NewImage1 = (Images1[k][x:x+ShapeTuple[0], y:y+ShapeTuple[1]])
					NewImage0 = (Images0[k][x:x+ShapeTuple[0], y:y+ShapeTuple[1]])
					NewImages1.append(NewImage1)
					NewImages0.append(NewImage0)
				else:
					print("No White Pixels found :(")
		PosPixels = {}
	print("MultImg has finished\n")
	return [NewImages0, NewImages1]


def DataPrep(InputData0, InputData1, ImWidth, ImHeight, TestFraction=0):
	#takes images by pah, converts to grayscale aray, shuffles, splits
	print("DataPrep has began its journy")
	Training_Images0 = InputData0
	Training_Images1 = InputData1
	Test_Images0 = []
	Test_Images1 = []
	c = list(zip(Training_Images0, Training_Images1))
	random.shuffle(c)
	Training_Images0, Training_Images1 = zip(*c)
	Training_Images0, Training_Images1 = list(Training_Images0), list(Training_Images1)
	for i in range(int(len(Training_Images0)*TestFraction)):
		Test_Images0.append(Training_Images0[i])
		Training_Images0.pop(i)
		Test_Images1.append(Training_Images1[i])
		Training_Images1.pop(i)
	Training_Images0 = np.array(Training_Images0).reshape(-1, ImWidth, ImHeight, 3)
	print(Training_Images0[0].shape)
	print("DataPrep says byby\n")
	return Training_Images0

dat = LoadImg(DATADIR0, DATADIR1, 2560, 1440)
#[Im0, Im1]

dat1 = MultImg(dat[0], dat[1], 1, (512, 512))
#[Im0, Im1]

dat2 = DataPrep(dat1[0], dat1[1], 512, 512)
print(dat2[0].shape)
liste=[]

for dat in dat2:
	liste.append(dat.reshape(-1,512,512,3))

"""
print("pickle says hello")
pickle.dump(liste, open(DATADIR2, "wb"))
print("Le finish\n")
"""