from selenium_course.common_lib.calc import calc_x
from selenium import webdriver

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

current_window = browser.current_window_handle

button = browser.find_element_by_tag_name("button")
button.click()

for window in browser.window_handles:
  if not (window == current_window):
    browser.switch_to.window(window)

#confirm = browser.switch_to.alert
#confirm.accept()

x = browser.find_element_by_id('input_value')
x = x.text
y = calc_x(x)

input = browser.find_element_by_id('answer')
input.send_keys(y)

button = browser.find_element_by_tag_name("button")
button.click()
