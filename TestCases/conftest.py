import pytest
from selenium import webdriver

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriver, ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from PageObjects.loginPage import loginPage
from PageObjects.homePage import homePage

@pytest.fixture()
def setup(browser):
    if browser == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    elif browser == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    return driver



def pytest_addoption(parser):
    parser.addoption("--browser",help="Choose the browser: firefox or chrome")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")