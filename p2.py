import numpy as np 
import os
import cv2
from matplotlib import pyplot as plt
from PIL import Image as Pil_image, ImageTk as Pil_imageTk
import pickle
import random
from time import sleep, time

DATADIR0 = r"D:\K14\Dataset\Predicitions.pickle"

data = pickle.load(open(DATADIR0, "rb"))

pred = data[1][33]

NewImage0 = data[2]

# The image is only displayed if we call this
#NewImage0 = (pred[285:295, 190:200])
#px, py= 190, 250
#s = 5
#NewImage0 = (pred[py:py+s, px:px+s])
#cv2.imshow("r", NewImage0)
def Coords(Pred, small):
	#cv2, Predicitons.pickle[2]=small
	result = cv2.matchTemplate(Pred, small, cv2.TM_SQDIFF_NORMED)
	mn,_,mnLoc,_ = cv2.minMaxLoc(result)
	MPx,MPy = mnLoc
	#x and y may flipped
	return (MPx+2, MPy+2)

def Coords2(Pred, small):
	pred = Pred
	#cv2, Predicitons.pickle[2]=small
	result = cv2.matchTemplate(pred, small, cv2.TM_SQDIFF_NORMED)
	mn,_,mnLoc,_ = cv2.minMaxLoc(result)
	MPx,MPy = mnLoc
	trows,tcols = small.shape[:2]
	cv2.rectangle(pred, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,0),2)
	#x and y may flipped
	return pred
print(pred.shape)
MPx, MPy = Coords(pred, NewImage0)
print(MPx, MPy)
# Read the images from the file

# Step 2: Get the size of the template. This is the same size as the match.
trows,tcols = NewImage0.shape[:2]

# Step 3: Draw the rectangle on large_image
cv2.rectangle(pred, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,0),2)

# Display the original image with the rectangle around the match.
cv2.imshow('output',pred)

# The image is only displayed if we call this
cv2.waitKey(0)



"""

res = cv2.matchTemplate(pred, NewImage0, cv2.TM_SQDIFF)
threshhold = 1
loc = np.where(res >= threshhold)

x, y = 200, 200


for i in range(1):
	cv2.rectangle(pred, (loc[1][i] , loc[0][i]), (loc[1][i]+1 , loc[0][i]+1), (255,0,0), 1)


cv2.imshow("r", pred)
cv2.waitKey()
#cv2.waitKey()
"""

"""
data.append(NewImage0)

print("pickle says hello")
pickle.dump(data, open(DATADIR0, "wb"))
print("Le finish\n")
"""