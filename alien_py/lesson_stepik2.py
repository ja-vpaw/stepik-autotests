import selenium
from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get(" http://suninjuly.github.io/registration2.html")
first_name_input = driver.find_element_by_css_selector('body > div > form > div.first_block > div.form-group.first_class > input')
first_name_input.send_keys('aaa')
surname_input = driver.find_element_by_css_selector('body > div > form > div.first_block > div.form-group.second_class > input')
surname_input.send_keys('qqq')
email_input = driver.find_element_by_css_selector('body > div > form > div.first_block > div.form-group.third_class > input')
email_input.send_keys('aaaa@gmail.com')
button = driver.find_element_by_css_selector('body > div > form > button')
button.click()
time.sleep(3)
welcome_text_elt = driver.find_element_by_tag_name('h1')
welcome_text = welcome_text_elt.text
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text


