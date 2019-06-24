from selenium_course.common_lib.calc import calc_x
from selenium import webdriver

link = "https://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element_by_id('input_value')
x = x.text
y = calc_x(x)

input = browser.find_element_by_id('answer')
input.send_keys(y)

checkbox = browser.find_element_by_id('robotCheckbox')
checkbox.click()

browser.execute_script("window.scrollBy(0, 50);")

robot_radiobutton = browser.find_element_by_id('robotsRule')
robot_radiobutton.click()

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
