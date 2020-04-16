import pyautogui as pa

pa.moveTo(500,100, duration=3)
pa.click()
# pa.typewrite('Yo')

pa.hotkey('ctrl', 'n')
pa.typewrite("print('yee')")
pa.hotkey('ctrl','s')
