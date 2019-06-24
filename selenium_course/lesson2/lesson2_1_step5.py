from selenium_course.common_lib.calc import calc_x
from selenium import webdriver

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element_by_id('input_value')
x = x.text
y = calc_x(x)

input = browser.find_element_by_id('answer')
input.send_keys(y)

checkbox = browser.find_element_by_id('robotCheckbox')
checkbox.click()

robot_radiobutton = browser.find_element_by_id('robotsRule')
robot_radiobutton.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()


