import numpy as np 
import os
import cv2
from matplotlib import pyplot as plt
from PIL import Image as Pil_image, ImageTk as Pil_imageTk
import pickle
import random

DATADIR0 = r"C:\Users\8holz\Documents\GitHub\K14 Githubg\Dataset\K14 Prototyp 572x572\K14 Prototyp 572x572\ds0\img"
DATADIR1 = r"C:\Users\8holz\Documents\GitHub\K14 Githubg\Dataset\K14 Prototyp 572x572\K14 Prototyp 572x572\ds0\masks_machine"
DATADIR2 = r"C:\Users\8holz\Documents\GitHub\K14 Githubg\Dataset\K14 Prototyp 572x572\Prep.pickle"

def ImCompareGray(Im1, Im2, FigSize=(10,10)):
    f = plt.figure(figsize=FigSize)
    f.add_subplot(1,2, 1)
    plt.imshow(Im1, cmap="gray")
    f.add_subplot(1,2, 2)
    plt.imshow(Im2, cmap="gray")
    plt.show(block=True)

def MultiplyImages(InputDir0, InputDir1, ImWidth, ImHeight, TestFraction=0.25):
	#takes images by pah, converts to grayscale aray, shuffles, splits
	Images0 = []
	Images1 = []
	for i in range(len(os.listdir(InputDir0))):
		array = cv2.imread(os.path.join(InputDir0, os.listdir(InputDir0)[i]), cv2.IMREAD_GRAYSCALE)
		Images0.append(array)
		break
	for i in range(len(os.listdir(InputDir1))):
		array = cv2.imread(os.path.join(InputDir1, os.listdir(InputDir1)[i]), cv2.IMREAD_GRAYSCALE)
		Images1.append(array)
		break
	return [
		Images0, 
		Images1,
		]

def MultImg(Images0, Images1, Multiplications, ShapeTuple):
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
			x = random.randrange(minx, maxx)
			y = random.randrange(miny, maxy)
			NewImage1 = (Images1[k][x:x+ShapeTuple[0], y:y+ShapeTuple[1]])
			NewImage0 = (Images0[k][x:x+ShapeTuple[0], y:y+ShapeTuple[1]])
			NewImages1.append(NewImage1)
			NewImages0.append(NewImage0)
	return [NewImages0, NewImages1]


dat = MultiplyImages(DATADIR0, DATADIR1, 572, 572)
dat1 = MultImg(dat[0], dat[1], 1, (100, 100))
print(dat1)
for i in range(1):
	ImCompareGray(dat1[0][i], dat1[1][i])