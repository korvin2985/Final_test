<<<<<<< Updated upstream
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en')


@pytest.fixture(scope="function")
def browser(request):
    language_name = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language_name})
    browser = webdriver.Chrome(executable_path="c:\chromedriver\chromedriver.exe", options=options)
    yield browser
    browser.quit()


=======
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en')


@pytest.fixture(scope="function")
def browser(request):
    language_name = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language_name})
    browser = webdriver.Chrome(executable_path="c:\chromedriver\chromedriver.exe", options=options)
    yield browser
    browser.quit()


>>>>>>> Stashed changes