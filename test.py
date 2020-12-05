import pyautogui
import time
pyautogui.FAILSAFE = False
while True:
    time.sleep(15)
    for i in range(5, 100):
        pyautogui.moveTo(100, i * 5)