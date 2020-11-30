import numpy as np 
import os
import cv2
from matplotlib import pyplot as plt
from PIL import Image as Pil_image, ImageTk as Pil_imageTk
import pickle
import random

DATADIR0 = r"D:\K14\Dataset\K14 Dataset-0\K14 Dataset-0\ds0\img"
DATADIR1 = r"D:\K14\Dataset\K14 Dataset-0\K14 Dataset-0\ds0\masks_machine"
DATADIR2 = r"D:\K14\Dataset\K14-Dataset-0-Multi.pickle"

def ImCompareGray(Im1, Im2, FigSize=(10,10)):
    f = plt.figure(figsize=FigSize)
    f.add_subplot(1,2, 1)
    plt.imshow(Im1, cmap="gray")
    f.add_subplot(1,2, 2)
    plt.imshow(Im2, cmap="gray")
    plt.show(block=True)

def LoadArray(InputDir0, InputDir1, ImWidth, ImHeight, TestFraction=0.25):
	#takes images by pah, converts to grayscale aray, shuffles, splits
	print("LoadArray is running")
	Images0 = []
	Images1 = []
	for i in range(len(os.listdir(InputDir0))):
		array = cv2.imread(os.path.join(InputDir0, os.listdir(InputDir0)[i]), cv2.IMREAD_GRAYSCALE)
		Images0.append(array)
	for i in range(len(os.listdir(InputDir1))):
		array = cv2.imread(os.path.join(InputDir1, os.listdir(InputDir1)[i]), cv2.IMREAD_GRAYSCALE)
		Images1.append(array)
	print("Loading succesful\n")
	return [Images0, Images1]

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
		print("Image: "+str(k)+" out of: "+str(len(Images1)))
		rows,cols = Images1[k].shape
		for i in range(rows):
			for j in range(cols):
				if Images1[k][i,j] == 1:
					PosPixels.update({i:j})
		for m in range(Multiplications):
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
			try:
				x = random.randrange(minx, maxx)
				y = random.randrange(miny, maxy)
			except ValueError:
				print("Value Error")
				x = random.randrange(minx, maxx+1)
				y = random.randrange(miny, maxy+1)
			NewImage1 = (Images1[k][x:x+ShapeTuple[0], y:y+ShapeTuple[1]])
			NewImage0 = (Images0[k][x:x+ShapeTuple[0], y:y+ShapeTuple[1]])
			NewImages1.append(NewImage1)
			NewImages0.append(NewImage0)
	print("Multiplying succesful")
	return [NewImages0, NewImages1]

def DataPrep(InputDat0, InputDat1, ImWidth, ImHeight, TestFraction=0.25):
	#takes images by pah, converts to grayscale aray, shuffles, splits
	Training_Images0 = InputDat0
	Training_Images1 = InputDat1
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
	Training_Images0 = np.array(Training_Images0).reshape(-1, ImWidth, ImHeight, 1)
	Training_Images1 = np.array(Training_Images1).reshape(-1, ImWidth, ImHeight, 1)
	Test_Images0 = np.array(Test_Images0).reshape(-1, ImWidth, ImHeight, 1)
	Test_Images1 = np.array(Test_Images1).reshape(-1, ImWidth, ImHeight, 1)
	return {
		"TrainImages0":Training_Images0, 
		"TrainImages1":Training_Images1,
		"TestImages0":Test_Images0,
		"TestImages1":Test_Images1
		}


dat = LoadArray(DATADIR0, DATADIR1, 2560, 1440)
dat = MultImg(dat[0], dat[1], 10, (512, 512))
dat = DataPrep(dat[0], dat[1], 512, 512)

f = open(DATADIR2, "wb")
pickle.dump(dat, f)