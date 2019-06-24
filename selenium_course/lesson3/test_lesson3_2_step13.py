import unittest
from selenium import webdriver
import time

class TestAbs(unittest.TestCase):
    browser = webdriver.Chrome()

    def test_page_registration1(self):

        link = "http://suninjuly.github.io/registration1.html"
        self.browser.get(link)

        self.fill_required_input()

        welcome_text = self.text_from_success_login_page()

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text)
        time.sleep(1)

    def test_page_registration2(self):

        link = "http://suninjuly.github.io/registration2.html"
        self.browser.get(link)

        self.fill_required_input()

        welcome_text = self.text_from_success_login_page()

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text)
        time.sleep(1)

    def text_from_success_login_page(self):
        # Проверяем, что смогли зарегистрироваться и ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        return welcome_text

    def fill_required_input(self):
        # Код, который заполняет обязательные поля
        input_name = self.browser.find_element_by_css_selector('.first_block  .first')
        input_name.send_keys("Ivan")
        input_surname = self.browser.find_element_by_css_selector('.first_block  .second')
        input_surname.send_keys("Petrov")
        input_email = self.browser.find_element_by_css_selector('.first_block  .third')
        input_email.send_keys("ivan@petrov.com")
        # Отправляем заполненную форму
        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()


if __name__ == '__main__':
    unittest.main()
