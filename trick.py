import pyautogui
import random
import time

def getRandDelay(min, max):
    delay = round(random.uniform(min, max), 2)
    return delay

def randomMouseMove():
    num = random.randint(1, 10)

    if (num == 7):
        x, y = pyautogui.position()
        pyautogui.moveTo(random.randint(1,1000), random.randint(1,500))
        time.sleep(getRandDelay(1,2))
        pyautogui.moveTo(x,y)