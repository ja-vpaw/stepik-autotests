import os
from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)


required_field = browser.find_elements_by_css_selector('input[type="text"]')
for field in required_field:
        field.send_keys('Test')

file_send_btn = browser.find_element_by_css_selector('input[type="file"]')
file_send_btn.send_keys(os.path.abspath('bio.txt'))

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()
