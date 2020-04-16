import pyautogui as pa
import time 

pa.moveTo(50,50, duration=2)
time.sleep(1)
pa.typewrite("google chrome")
time.sleep(1)
pa.hotkey('enter')
time.sleep(3)
pa.typewrite("ecosia.org")
pa.hotkey('enter')
pa.typewrite("ad")