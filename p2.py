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

def data_prep(InputDir0, InputDir1, ImWidth, ImHeight, TestFraction=0.25):
	#takes images by pah, converts to grayscale aray, shuffles, splits
	Training_Images0 = []
	Training_Images1 = []
	Test_Images0 = []
	Test_Images1 = []
	for i in range(len(os.listdir(InputDir0))):
		array = cv2.imread(os.path.join(InputDir0, os.listdir(InputDir0)[i]), cv2.IMREAD_GRAYSCALE)
		Training_Images0.append(array)
	for i in range(len(os.listdir(InputDir1))):
		array = cv2.imread(os.path.join(InputDir1, os.listdir(InputDir1)[i]), cv2.IMREAD_GRAYSCALE)
		Training_Images1.append(array)
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

dat = data_prep(DATADIR0, DATADIR1, 572, 572)
f = open(DATADIR2, "wb")
pickle.dump(dat, f)