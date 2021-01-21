import os
import pickle
from threading import Thread
import time
from matplotlib import pyplot as plt
from ctypes import windll
from math import ceil, floor

StopKey = True

distx =0
disty =0
strength =1
Exceptions =[]
MaxIterations =3

def MouseControlV3(distx, disty, strength=1, Exceptions=[], MaxIterations=6):
    #32 directions, 512 distances, 1 Iteration = 0.015
    x = distx*strength
    y = disty*strength
    print(x,y)
    if x not in Exceptions or y not in Exceptions:
        if min(x,y)<=1:
            windll.user32.mouse_event(0x0001, int(x), int(y), 0, 0)
        else:
            if min(x,y)>MaxIterations:
                Iterations = 6
            else:
                Iterations=ceil(min(x,y))
            x1 = floor(x/(Iterations-1))
            y1 = floor(y/(Iterations-1))
            for i in range(Iterations-1):
                windll.user32.mouse_event(0x0001, x1, y1, 0, 0)
                time.sleep(0.005)
            windll.user32.mouse_event(0x0001, int(x)-(x1*Iterations-1), int(y)-(y1*Iterations-1), 0, 0)

class MouseControlV4(Thread):
	def __init__(self):
		Thread.__init__(self)
		None
	def run(self):
	    #32 directions, 512 distances, 1 Iteration = 0.015
		global distx, disty, strength, Exceptions, MaxIterations
		Ldistx, Ldisty = distx, disty
		while StopKey:
			if Ldistx != distx or Ldisty != disty:
				t = time.time()
				Ldistx = distx
				Ldisty = disty
				Lstrength = strength
				LExceptions = Exceptions
				LMaxIterations = MaxIterations
				x = distx*strength
				y = disty*strength
				print(x,y)
				if x not in Exceptions or y not in Exceptions:
					if min(x,y)<=1:
						windll.user32.mouse_event(0x0001, int(x), int(y), 0, 0)
					else:
						if min(x,y)>MaxIterations:
							Iterations = 6
						else:
							Iterations=ceil(min(x,y))
						x1 = floor(x/(Iterations-1))
						y1 = floor(y/(Iterations-1))
						for i in range(Iterations-1):
							windll.user32.mouse_event(0x0001, x1, y1, 0, 0)
							time.sleep(0.005)
						windll.user32.mouse_event(0x0001, int(x)-(x1*Iterations-1), int(y)-(y1*Iterations-1), 0, 0)
				print(time.time()-t)


it = MouseControlV4()
it.start()
for i in range(10):
	distx, disty = distx+10, disty+10
	print(distx, disty)
	time.sleep(1)
StopKey = False
