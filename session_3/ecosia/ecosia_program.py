import pyautogui as pa
import time

pa.hotkey('win')
time.sleep(1)
pa.typewrite('chrome')
time.sleep(1)
pa.hotkey('enter')
time.sleep(2)

num_loops = int(pa.prompt(
	title='Loop number',
	text='How many times would you like to loop? '))
pa.moveTo(148, 261)
for looper in range(0,num_loops):
	pa.hotkey('ctrl', 't')
	pa.typewrite('https://www.ecosia.org/search?q=ads')
	pa.hotkey('enter')
	time.sleep(3)
	pa.click()

time.sleep(4)
pa.moveTo(1593, 7, duration=1)
pa.click()
