from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# Keys.ENTER
# from selenium.common.exceptions import StaleElementReferenceException

import time

opts = Options()
opts.headless = False

assert opts.set_headless

browser = Chrome(
	executable_path = 'C:/Users/Gregory Hall/Documents/Drivers/chromedriver.exe',
	options=opts)

browser.get('freerice url')
time.sleep(10)

# input_field = browser.find_element_by_tag_name('input')
# input_field.send_keys('ads')
# input_field.submit()
# time.sleep(3)

# ['ad1', 'ad2', 'ad3']

mult_category = browser.find_elements_by_class_name('category-item')[21]
text = mult_category.text
mult_category.click()
time.sleep(3)

question = browser.find_elements_by_class_name('')
question_txt = question.text
print (question_txt)

list_of_ads = browser.find_elements_by_class_name('result-title-ad')
first_ad = list_of_ads[0]
first_ad.click()

time.sleep(3)
# find_elements_by_class_name('')
# result-title-ad

# send_keys
# submit()
# click()

browser.quit()