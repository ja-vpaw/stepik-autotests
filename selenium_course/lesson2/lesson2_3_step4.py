from selenium_course.common_lib.calc import calc_x
from selenium import webdriver

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)


button = browser.find_element_by_tag_name("button")
button.click()

confirm = browser.switch_to.alert
confirm.accept()

x = browser.find_element_by_id('input_value')
x = x.text
y = calc_x(x)

input = browser.find_element_by_id('answer')
input.send_keys(y)

button = browser.find_element_by_tag_name("button")
button.click()
