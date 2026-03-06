import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class FlighBookingPage:
    def __init__(self,driver):
        self.driver = driver
        self.radio_options=(By.CSS_SELECTOR, "table.tblTrip input")
        self.discountCheckbox=(By.CSS_SELECTOR, "#discount-checkbox div input")
        self.departure_city=(By.XPATH,"//input[@id='ctl00_mainContent_ddl_originStation1_CTXT']")
        self.arrival_city=(By.XPATH,"//input[@id='ctl00_mainContent_ddl_destinationStation1_CTXT']")
        self.select_arrival_city=(By.XPATH,"//div[@class='dropdownDiv']/ul/li/a")
        self.dropdown_option=(By.CSS_SELECTOR,".row1.adult-infant-child")
        self.passesngers_dropdown=(By.XPATH,"//div[@class='row1 adult-infant-child']/div[3]/div")
        self.searchButton=(By.ID,"ctl00_mainContent_btn_FindFlights")
        self.add_adult=(By.XPATH,"//div/span[@id='hrefIncAdt']")
        self.doneBtn=(By.ID,"btnclosepaxoption")


    def select_radiobutton(self,trip):
        self.wait = WebDriverWait(self.driver, 10)
        self.wait.until(expected_conditions.visibility_of_all_elements_located(
            (self.radio_options)
        ))
        options = self.driver.find_elements(*self.radio_options)
        print(len(options))
        for option in options:
            if option.get_attribute("value") == trip:
                option.click()
                assert option.is_selected()
                time.sleep(2)
                break
    def select_checkbox(self,option):
        self.wait.until(expected_conditions.visibility_of_all_elements_located(
            (self.discountCheckbox)))
        checkboxes = self.driver.find_elements(*self.discountCheckbox)
        print(len(checkboxes))
        for checkbox in checkboxes:
            if checkbox.get_attribute("name") == option:
                checkbox.click()
                time.sleep(2)
                assert checkbox.is_selected()
                break
    def fill_details(self,deptcity,arrivalcity):
        self.driver.find_element(*self.departure_city).send_keys(deptcity)
        self.driver.find_element(*self.arrival_city).send_keys(arrivalcity)
        arrival_cities=self.driver.find_elements(*self.select_arrival_city)
        print(len(arrival_cities))
        for city in arrival_cities:
            if city.text==arrivalcity:
                city.click()
                break
        # self.driver.find_element(*self.departDateCalendar).click()
        time.sleep(2)
        # self.wait.until(expected_conditions.presence_of_element_located(self.dropdown_option))
        # self.driver.find_element(*self.dropdown_option).click()


        # self.wait.until(expected_conditions.presence_of_element_located(self.add_adult))
        # self.driver.find_element(*self.add_adult).click()
        # self.driver.find_element(*self.doneBtn).click()
        # time.sleep(2)
        #

    def searchFlight(self):
        self.driver.find_element(*self.searchButton).click()



