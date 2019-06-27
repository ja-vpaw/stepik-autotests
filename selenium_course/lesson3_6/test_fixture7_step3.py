import pytest
import time, math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

links = ["https://stepik.org/lesson/236895/step/1",
         "https://stepik.org/lesson/236896/step/1",
         "https://stepik.org/lesson/236897/step/1",
         "https://stepik.org/lesson/236898/step/1",
         "https://stepik.org/lesson/236899/step/1",
         "https://stepik.org/lesson/236903/step/1",
         "https://stepik.org/lesson/236904/step/1",
         "https://stepik.org/lesson/236905/step/1"
        ]

@pytest.fixture(scope="session")
def browser():
    print("\nstart browser for test..")
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option('w3c', False)
    browser = webdriver.Chrome(chrome_options=opt)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', links)
def test_guest_should_see_login_link(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/{}/".format(language)
    browser.get(link)
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.textarea'))
        )
    answer = math.log(int(time.time()))
    input = browser.find_element_by_css_selector(".textarea")
    input.send_keys(str(answer))

    button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
            )
    button.click()

    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
    )
    assert element.text == "Correct!"
