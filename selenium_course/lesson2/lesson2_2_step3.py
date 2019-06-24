from selenium import webdriver
from selenium.webdriver.support.ui import Select


p = None
count=0
while p not in ["1","2"]:
    if count >= 5:
        print("Завершение теста из-за некорректных входных данных")
        exit()
    p = input("Введите номер страницы [1,2]: ")
    count+=1

link = "http://suninjuly.github.io/selects"+p+".html"
browser = webdriver.Chrome()
browser.get(link)

num1, num2 = browser.find_element_by_id('num1') , browser.find_element_by_id('num2')
num1, num2 = num1.text, num2.text

sum = int(num1) + int(num2)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(sum))

#browser.find_element_by_tag_name("select").click()
#browser.find_element_by_css_selector("[value='1']").click()

button = browser.find_element_by_css_selector("button.btn")
button.click()
