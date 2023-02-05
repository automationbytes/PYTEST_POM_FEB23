from selenium.webdriver.common.by import By


class loginPage:

    #login
    username_textbox_id = "Email"
    password_textbox_id = "Password"
    login_button_xpath = "//button[text()='Log in']"

    def __init__(self,driver):
        self.driver = driver

    def enterUserName(self,username):

        self.driver.find_element(By.ID,self.username_textbox_id).clear()
        self.driver.find_element(By.ID,self.username_textbox_id).send_keys(username)


    def enterpassword(self,password):

        self.driver.find_element(By.ID,self.password_textbox_id).clear()
        self.driver.find_element(By.ID,self.password_textbox_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()