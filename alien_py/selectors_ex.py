import time
from selenium import webdriver

good_link = "http://suninjuly.github.io/registration1.html"
bad_link = "http://suninjuly.github.io/registration2.html"

browser = webdriver.Chrome()
# browser.get(good_link)
browser.get(bad_link)

fields = ['first', 'second', 'third']
for field in fields:
    required_field = browser.find_element_by_css_selector("input:required[class$='{}']".format(field))
    required_field.send_keys('Test')

button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(1)

welcome_text_elt = browser.find_element_by_tag_name("h1")
welcome_text = welcome_text_elt.text

assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text