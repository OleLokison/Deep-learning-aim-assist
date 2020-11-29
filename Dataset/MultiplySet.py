import numpy as np 
import os
import cv2
from matplotlib import pyplot as plt
from PIL import Image as Pil_image, ImageTk as Pil_imageTk
import pickle
import random

DATADIR0 = r"D:\K14\Dataset\K14 Prototyp 572x572\K14 Prototyp 572x572\ds0\img"
DATADIR1 = r"D:\K14\Dataset\K14 Prototyp 572x572\K14 Prototyp 572x572\ds0\masks_machine"
DATADIR2 = r"D:\K14\Dataset\K14 Prototyp 572x572\Prep.pickle"

def ImCompareGray(Im1, Im2, FigSize):
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

def MultImg(Images0, Images1, ShapeTuple):
	TestImg = random.choice(Images0), random.choice(Images1)
	if (ShapeTuple[0] > random.choice(TestImg[0]).shape[0] or 
		ShapeTuple[0] > random.choice(TestImg[1]).shape[0] or 
		ShapeTuple[1] > random.choice(TestImg[0]).shape[1] or 
		ShapeTuple[1] > random.choice(TestImg[1]).shape[1]):
		print("ShapeTuple is to Big for Operation")
		return
	PosPixels = {}
	NewImages0 = []
	NewImages1 = []
	PosArea = {
		"xmin":ShapeTuple[0], 
		"ymin":ShapeTuple[1]}
	for i in range(len(Images1)):
		rows,cols = Images1[i].shape
		break
		for i in range(rows):
			for j in range(cols):
				if Images1[i][i,j] == 1:
					PosPixels.update({i:j})
		Pickedi, Pickedj = random.choice(list(PosPixels.items()))
		if Pickedi < ShapeTuple[0]:
			Pickedi = ShapeTuple[0]
		if Pickedj < ShapeTuple[1]:
			Pickedj = ShapeTuple[1]
		#
		NewImages0.append(Images0[y:y+h, x:x+w])

dat = MultiplyImages(DATADIR0, DATADIR1, 572, 572)
MultImg(dat[0], dat[1], (100, 100))