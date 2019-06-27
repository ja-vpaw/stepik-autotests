import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption("browser_name")

    def chrome_setup():
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('w3c', False)
        browser = webdriver.Chrome(chrome_options=opt)
        return browser

    print("\nstart browser for test..")
    if browser_name == "chrome":
        browser = chrome_setup()
    elif browser_name == "firefox":
        browser = webdriver.Firefox()
    else:
        print("Browser {} still is not implemented".format(browser_name))
        raise Exception

    yield browser

    print("\nquit browser..")
    browser.quit()
