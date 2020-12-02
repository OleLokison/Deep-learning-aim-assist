import numpy as np 
import os
import cv2
from matplotlib import pyplot as plt
from PIL import Image as Pil_image, ImageTk as Pil_imageTk
import pickle
import random

DATADIR0 = r"D:\K14\Dataset\K14 Dataset-seg\K14 Dataset-0\ds0\img"
DATADIR1 = r"D:\K14\Dataset\K14 Dataset-seg\K14 Dataset-0\ds0\masks_machine"
DATADIR2 = r"D:\K14\Dataset\K14-Dataset-0-Multi.pickle"

def ImCompareGray(Im1, Im2, FigSize=(10,10)):
    f = plt.figure(figsize=FigSize)
    f.add_subplot(1,2, 1)
    plt.imshow(Im1, cmap="gray")
    f.add_subplot(1,2, 2)
    plt.imshow(Im2, cmap="gray")
    plt.show(block=True)

dat = pickle.load(open(DATADIR2, "rb"))

for i in range(15):
	ImCompareGray(dat["TestImages0"][i], dat["TestImages1"][i])

