import pytest
'''
to run
pytest -v -s --html-report=../report/report.html --browser chrome

'''

from selenium import webdriver

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriver, ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from PageObjects.loginPage import loginPage
from PageObjects.homePage import homePage

from Config.PropReader import propfile, PropReader
prpreader = PropReader()


class TestDemo:
    @pytest.fixture()
    def pretest(self, setup):

        self.driver = setup
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        print(PropReader.readProp("url"))

        self.driver.get(PropReader.readProp("url"))
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        lp = loginPage(self.driver)
        lp.enterUserName(PropReader.readProp("username"))
        lp.enterpassword(PropReader.readProp("password"))
        lp.clickLogin()

    def test_verifydashboard(self, pretest):
        hp = homePage(self.driver)
        if hp.verifydashboardheader():
            assert True
        else:
            self.driver.save_screenshot("logo.png")
            assert False

    def test_logout(self, pretest):
        hp = homePage(self.driver)
        hp.clickLogout()



