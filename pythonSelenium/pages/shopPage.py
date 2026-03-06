from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pythonSelenium.pages.checkout_confirmation import checkout_confirmation
from pythonSelenium.utility.browserUtils import browserUtils


class ShopPage(browserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.ShopButton=(By.CSS_SELECTOR, "a[href*='shop']")
        self.items=(By.XPATH, "//div[@class='card h-100']")
        self.model=(By.XPATH, ".//h4/a")
        self.addtoCartButton=(By.XPATH, ".//button[text()='Add ']")
        self.buttonText=(By.XPATH, "//a[@class='nav-link btn btn-primary']")

    def addItemtoCart(self,Item):
        self.driver.find_element(*self.ShopButton).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((self.items)))
        mobiles = self.driver.find_elements(*self.items)
        print(len(mobiles))
        model_names = []
        # css= a[href*='shop'] xpath=//a[contains(@href, 'shop')]

        for mobile in mobiles:
            model = mobile.find_element(*self.model).text
            self.driver.execute_script("window.scrollTo(0,3000)")
            if model == Item:
                mobile.find_element(*self.addtoCartButton).click()

    def click_CheckoutButton(self):

        self.driver.execute_script("window.scrollTo(0,10)")
        button_text = self.driver.find_element(*self.buttonText).text
        print(button_text)
        self.driver.find_element(*self.buttonText).click()
        checkoutConfirmation=checkout_confirmation(self.driver)
        return checkoutConfirmation