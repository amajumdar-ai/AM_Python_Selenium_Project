from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pythonSelenium.pages.shopPage import ShopPage
from pythonSelenium.utility.browserUtils import browserUtils


class LoginPage(browserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username=(By.CSS_SELECTOR, ".form-control")
        self.password=(By.XPATH, "//input[@type='password']")
        self.dropdown=(By.XPATH, "//select[@class='form-control']")
        self.term=(By.ID, 'terms')
        self.signInBtn=(By.XPATH, "//input[@id='signInBtn']")

    def loginPage(self,username,password):
        self.driver.find_elements(*self.username)[0].send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.dropdown = Select(self.driver.find_element(*self.dropdown))
        self.dropdown.select_by_index(1)
        self.driver.find_element(*self.term).click()
        self.driver.find_element(*self.signInBtn).click()
        shopPage=ShopPage(self.driver)
        return shopPage