from time import time, sleep
from ctypes import windll
from math import sin, cos, radians, sqrt, floor, ceil


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

distx, disty = 0, 0
strength = 0.4
Exceptions = [-76.2, 33.3, -35.699999999999996, 77.0, -88.5, -127.0, -97.5, 32.5, -21.5, -68.0]
MaxIterations = 3

def MouseControlV5():
    global distx, disty, strength, Exceptions, MaxIterations
    Ldistx, Ldisty = 0, 0
    if Ldistx != distx or Ldisty != disty:
        #t = time()
        Ldistx = distx
        Ldisty = disty
        Lstrength = strength
        LExceptions = Exceptions
        LMaxIterations = MaxIterations
        x = distx*strength
        y = disty*strength
        #print(x,y)
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
        #print(time()-t)
    sleep(0.05)

distx, disty = 100, 0
strength = 0.4

t = time()
MouseControlV5()
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