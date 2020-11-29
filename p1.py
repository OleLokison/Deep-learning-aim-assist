import numpy
import os
import cv2
from matplotlib import pyplot as plt
from PIL import Image as Pil_image, ImageTk as Pil_imageTk
import pickle

def Cropper(Path, x, y):
	#gets cutten centered, var represents length
	image = Pil_image.open(Path)
	width, height = image.size
	TopLeftx, TopLefty 			= (width-x)/2, (height-y)/2
	BottomRightx, BottomRighty 	= (width-x)/2+x, (height-y)/2+y
	im_crop = image.crop((TopLeftx, TopLefty, BottomRightx, BottomRighty))
	return im_crop


DATADIR0 = r"D:\K14\Dataset\K14 Prototyp 572x572\K14 Prototyp 572x572\ds0\img"
DATADIR1 = r"D:\K14\Dataset\K14 Prototyp 572x572\K14 Prototyp 572x572\ds0\masks_machine"


im0 = os.listdir(DATADIR0)[10]
im1 = os.listdir(DATADIR1)[10]



im_array0 = cv2.imread(os.path.join(DATADIR0, im0), cv2.IMREAD_GRAYSCALE)
im_array1 = cv2.imread(os.path.join(DATADIR1, im1), cv2.IMREAD_GRAYSCALE)

def ImCompareGray(Im1, Im2):
	f = plt.figure()
	f.add_subplot(1,2, 1)
	plt.imshow(Im1, cmap="gray")
	f.add_subplot(1,2, 2)
	plt.imshow(Im2, cmap="gray")
	plt.show(block=True)


def data_prep(InputDir0, InputDir1, OutputDirTrain, OutputDirTest, TestFraction=0.25):
	Training_Images0 = []
	Training_Images1 = []
	Test_Images0 = []
	Test_Images1 = []
	for i in range(len(os.listdir(InputDir0))):
		array = im.cv2.imread(os.listdir(InputDir0)[i], cv2.IMREAD_GRAYSCALE)
		array.append(Test_Images0)
	for im in os.listdir(InputDir1):
		array = im.cv2.imread(im, cv2.IMREAD_GRAYSCALE)
		array.append(Test_Images0)