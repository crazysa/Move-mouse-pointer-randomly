import pyautogui
import random
import time 



s = pyautogui.size()  

while(True):
	p = pyautogui.position()
	movex , movey = random.randint(-200,200), random.randint(-200,200)
	if p[0]+movex <= 0 or p[0]+movex >= s[0]:
		movex = -(movex)
		
	elif p[1]+movey <= 0 or p[1]+movey >= s[1]:
		movey = -movey
		
	try:	
		pyautogui.moveRel(movex,movey ,  duration = 0)
	except:
		print(p , s , movex , movey)
		break
#	time.sleep(3)
#	
#	if p[0] < 100 or p[1] < 100:
#		pyautogui.moveRel(100, 100, duration = 1.2)
#	elif p[0] > s[0]-100 or p[1] > s[1]-100:
#		pyautogui.moveRel(-100, -100, duration = 1.2)

#while(True):
#	pyautogui.moveRel(random.randint(-100,100), random.randint(-100,100), duration = 1.2)
#	time.sleep(3)
#	p = pyautogui.position()
#	if p[0] < 100 or p[1] < 100:
#		pyautogui.moveRel(100, 100, duration = 1.2)
#	elif p[0] > s[0]-100 or p[1] > s[1]-100:
#		pyautogui.moveRel(-100, -100, duration = 1.2)
	