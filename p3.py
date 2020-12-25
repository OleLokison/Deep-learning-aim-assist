import numpy as np 
import os
import cv2
from matplotlib import pyplot as plt
from PIL import Image
import pickle
import random

DATADIR0 = r"D:\K14\Dataset\TestImagesScaled"
DATADIR2 = r"D:\K14\Dataset\TestImages.pickle"

f = pickle.load(open(DATADIR2, "rb"))

def ImCompareGray(Im1, Im2, FigSize=(10,10)):
    f = plt.figure(figsize=FigSize)
    f.add_subplot(1,2, 1)
    plt.imshow(Im1)
    f.add_subplot(1,2, 2)
    plt.imshow(Im2, "gray")
    plt.show(block=True)

for i in range(10, 20,1):
	ImCompareGray(f[0][i], f[1][i])