from selenium.webdriver.common.by import By


class homePage:
    dashboard_header_xpath = "//h1[contains(text(),'Dashboard')]"
    logout_button_xpath = "//a[text()='Logout']"

    def __init__(self,driver):
        self.driver = driver

    def verifydashboardheader(self):
        return self.driver.find_element(By.XPATH,self.dashboard_header_xpath).is_displayed()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.logout_button_xpath).click()



