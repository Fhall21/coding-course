import pyautogui as pa

# pa.moveTo(500,100, duration=3)
# pa.click()
# pa.typewrite('Yo')

user_input = pa.prompt('This lets the user type in a string and press OK.')
print (user_input)