from selenium import webdriver
import time

p = None
count=0
while p not in ["1","2"]:
    if count >= 5:
        print("Завершение теста из-за некорректных входных данных")
        exit()
    p = input("Введите номер страницы [1,2]: ")
    count+=1

link = "http://suninjuly.github.io/registration"+p+".html"
browser = webdriver.Chrome()
browser.get(link)

# Код, который заполняет обязательные поля
input_name = browser.find_element_by_css_selector('.first_block  .first')
input_name.send_keys("Ivan")

input_surname = browser.find_element_by_css_selector('.first_block  .second')
input_surname.send_keys("Petrov")

input_email = browser.find_element_by_css_selector('.first_block  .third')
input_email.send_keys("ivan@petrov.com")


# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться и ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
time.sleep(1)
browser.quit()
