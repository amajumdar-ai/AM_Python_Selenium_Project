import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class checkout_confirmation:
    def __init__(self, driver):
        self.driver = driver
        self.price=(By.XPATH, "//tr[2]/td[5]/h3")
        self.checkoutbutton=(By.XPATH, "//button[@class='btn btn-success']")
        self.country=(By.ID, "country")
        self.countries=(By.CSS_SELECTOR, "div.suggestions li a")
        self.selectedCountry=(By.CSS_SELECTOR, "div.suggestions li a")
        self.checkbox=(By.CSS_SELECTOR, ".checkbox.checkbox-primary")
        self.purchaseButton=(By.XPATH, "//input[@value='Purchase']")
        self.success_toaster_locator=(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
        self.success_toaster_dismiss=(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible a")

    def Final_Checkout_Button(self):
        total_price = self.driver.find_element(*self.price).text
        print(total_price)

    def country_selection(self,countryName):
        self.driver.find_element(*self.checkoutbutton).click()
        self.driver.find_element(*self.country).send_keys(countryName)
        self.wait = WebDriverWait(self.driver, 10)
        self.wait.until(expected_conditions.visibility_of_all_elements_located((self.countries)))
        countries = self.driver.find_elements(*self.selectedCountry)
        print(len(countries))
        for country in countries:
            if country.text == "India":
                country.click()
                break
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.purchaseButton).click()
        time.sleep(2)

    def success_toaster(self):
        return self.driver.find_element(*self.success_toaster_locator).text

