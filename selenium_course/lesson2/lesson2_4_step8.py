from selenium_course.common_lib.calc import calc_x

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

opt = webdriver.ChromeOptions()
opt.add_experimental_option('w3c', False)
browser = webdriver.Chrome(chrome_options=opt)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
WebDriverWait(browser, 30).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000")
    )
button = browser.find_element_by_id("book")
button.click()

x = browser.find_element_by_id('input_value')
x = x.text
y = calc_x(x)

input = browser.find_element_by_id('answer')
input.send_keys(y)

button = browser.find_element_by_id("solve")
button.click()
