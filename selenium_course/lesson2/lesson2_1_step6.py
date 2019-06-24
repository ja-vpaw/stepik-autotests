from selenium import webdriver


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)


human_radio = browser.find_element_by_id("humanRule")

human_checked = human_radio.get_attribute("checked")
print("value of human radio: ", human_checked)
assert human_checked is not None, "Human radio is not selected by default"

#assert human_checked == "true", "Human radio is not selected by default"

robots_radio = browser.find_element_by_id("robotsRule")
robots_checked = robots_radio.get_attribute("checked")
print("value of robots radio: ", robots_checked)
assert robots_checked is None

browser.quit()