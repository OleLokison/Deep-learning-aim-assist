import pyautogui as py 
import time 
import numpy as np
from matplotlib import pyplot as plt
"""
for i in range(10):
	print(py.position())
	time.sleep(1)
"""

a = py.screenshot(region=(1024, 464, 512, 512))
print(np.array(a).shape)

def ImCompareGray(Im1, Im2, FigSize=(10,10)):
    f = plt.figure(figsize=FigSize)
    f.add_subplot(1,2, 1)
    plt.imshow(Im1, "gray")
    f.add_subplot(1,2, 2)
    plt.imshow(Im2)
    plt.show(block=True)
ImCompareGray(a,a)