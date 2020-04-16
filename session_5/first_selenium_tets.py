from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
opts = Options()
opts.headless = False
assert opts.set_headless
browser = Chrome(
	executable_path="C:/Users/Gregory Hall/Documents/Drivers/chromedriver.exe", 
	options=opts)

browser.get('https://ecosia.org')
input_field = browser.find_element_by_tag_name('input') 
input_field.send_keys('ads')
input_field.submit()
time.sleep(1)

'''
username = browser.find_element_by_id('id_username')
password = browser.find_element_by_id('id_password')
submit = browser.find_element_by_tag_name('form')

username.send_keys('fhall21')
password.send_keys('mypassword')
submit.submit()
print ('entered')
'''
browser.quit()