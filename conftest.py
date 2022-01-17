import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language.")
    parser.addoption('--time_stop', action='store', default=0,
                     help="Включение паузы после загрузки")

@pytest.fixture(scope="function")
def pause_time(request):
    pause_mode = request.config.getoption("pause")
    return pause_mode

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser = None
    print("\nstart chrome browser for test..")
    options = Options()
    options.add_experimental_option('prefs',{'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(12)
    yield browser
    print("\nquit browser..")
    browser.quit()
