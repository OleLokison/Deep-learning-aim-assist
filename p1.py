import pyautogui as py
from time import sleep, time


filepath0 = r"C:\Users\8holz\Desktop\Test\runningicon.png"
filepath1 = r"C:\Users\8holz\Desktop\Test\Restart1.png"
filepath2 = r"C:\Users\8holz\Desktop\Test\Restart2.png"
filepath3 = r"C:\Users\8holz\Desktop\Test\Restart3.png"
filepath4 = r"C:\Users\8holz\Desktop\Test\blue.png"
filepath5 = r"C:\Users\8holz\Desktop\Test\ok0.png"
filepath6 = r"C:\Users\8holz\Desktop\Test\ok1.png"
Runtime = 50000
Count=0
Count1=3600

def RunAll():
	py.keyDown('ctrl')
	py.keyDown('alt')
	py.press('p')
	py.keyUp('ctrl')
	py.keyUp('alt')

t=time()
while (time()-t<Runtime):
	if py.locateOnScreen(filepath0)==None:
		print("Notebook has finished: "+str(Count))
		try:
			PosRestart1 = py.locateOnScreen(filepath1)[0]+10, py.locateOnScreen(filepath1)[1]+10
			py.moveTo(PosRestart1)
			py.click()
			sleep(5)
		except:
			try:
				print("Restart Icon not found!skrrrr")
				PosRestart4 = py.locateOnScreen(filepath4)[0], py.locateOnScreen(filepath4)[1]
				py.moveTo(PosRestart4)
				py.click()
				sleep(1)
			except:
				print("we kinda lost-------------------")
	else:
		print("Still running")
		sleep(60)
	try:
		PosRestart2 = py.locateOnScreen(filepath2)[0]+20, py.locateOnScreen(filepath2)[1]+15
		py.moveTo(PosRestart2)
		py.click()
		sleep(5)
		RunAll()
		Count+=1
	except:
		try:
			PosRestart3 = py.locateOnScreen(filepath3)[0]+20, py.locateOnScreen(filepath3)[1]+15
			py.moveTo(PosRestart3)
			py.click()
			sleep(5)
			RunAll()
			Count+=1
		except:
			try:
				PosRestart4 = py.locateOnScreen(filepath4)[0], py.locateOnScreen(filepath4)[1]
				py.moveTo(PosRestart4)
				py.click()
				sleep(1)
			except:
				None
	try:
		PosRestart5 = py.locateOnScreen(filepath5)[0]+10, py.locateOnScreen(filepath5)[1]+10
		py.moveTo(PosRestart5)
		py.click()
		sleep(5)
		RunAll()
		Count+=1
	except:
		try:
			PosRestart6 = py.locateOnScreen(filepath6)[0]+10, py.locateOnScreen(filepath6)[1]+10
			py.moveTo(PosRestart6)
			py.click()
			sleep(5)
			RunAll()
			Count+=1
		except:
			try:
				PosRestart4 = py.locateOnScreen(filepath4)[0], py.locateOnScreen(filepath4)[1]
				py.moveTo(PosRestart4)
				py.click()
				sleep(1)
			except:
				None
	if (time()-t>Count1):
		Count1=Count1+1800
		try:
			PosRestart1 = py.locateOnScreen(filepath1)[0]+10, py.locateOnScreen(filepath1)[1]+10
			py.moveTo(PosRestart1)
			py.click()
			sleep(5)
		except:
			try:
				print("Restart Icon not found!bra")
				PosRestart4 = py.locateOnScreen(filepath4)[0], py.locateOnScreen(filepath4)[1]
				py.moveTo(PosRestart4)
				py.click()
				sleep(1)
			except:
				try:
					PosRestart1 = py.locateOnScreen(filepath1)[0]+10, py.locateOnScreen(filepath1)[1]+10
					py.moveTo(PosRestart1)
					py.click()
					sleep(5)
				except:
					print("we kinda lost-------------------")