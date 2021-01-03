from time import time, sleep
from ctypes import windll
from math import sin, cos, radians, sqrt, floor, ceil

def MouseControlV2(distx, disty, strength=1, velocity=10):
    #32 directions
    #512 distances
    x = floor(distx*strength)
    y = floor(disty*strength)
    distance = sqrt((x**2+y**2))
    iterations = int(distance/velocity)
    print(iterations)
    for i in range(iterations):
        windll.user32.mouse_event(0x0001, int(x/iterations), int(y/iterations), 0, 0)
        sleep(0.005)

def MouseControlV3(distx, disty, strength=1, MaxIterations=6):
    #32 directions, 512 distances, 1 Iteration = 0.015
    x = distx*strength
    y = disty*strength
    print(x,y)
    if min(x,y)<=1:
        windll.user32.mouse_event(0x0001, int(x), int(y), 0, 0)
    else:
        if min(x,y)>MaxIterations:
            Iterations = 6
        else:
            Iterations=floor(min(x,y))
        x1 = floor(x/(Iterations-1))
        y1 = floor(y/(Iterations-1))
        for i in range(Iterations-1):
            windll.user32.mouse_event(0x0001, x1, y1, 0, 0)
            sleep(0.005)
        windll.user32.mouse_event(0x0001, x-(x1*Iterations-1), y-(y1*Iterations-1), 0, 0)

t = time()
MouseControlV3(1, 0, 0.1)
print(time()-t)
"""
1/6 = 0.XX
ceil = 1
ceil-1 = Phase 1
x = distance - Phase1*(distance/ceil)
round(x)

250/60 = 4.3
ceil = 5
"""