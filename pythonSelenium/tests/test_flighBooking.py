import json

import pytest

from pythonSelenium.pages.loginPage import LoginPage
from pythonSelenium.pages.FlighBookingPage import FlighBookingPage
test_data_file="./data/test_flighBooking_data.json"
test_data_list=json.load(open(test_data_file))

with open(test_data_file) as f:
    test_data=json.load(f)
    test_data_list=test_data["flight_data"]


@pytest.mark.parametrize("test_data_item",test_data_list)

def test_flightBooking(browserInstance,test_data_item):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
    cb=FlighBookingPage(driver)
    # Select radio button
    cb.select_radiobutton("One Way")
    cb.fill_details(test_data_item["departure_city"],test_data_item["arrival_city"])
    # Checkbox selection
    cb.select_checkbox("ctl00$mainContent$chk_SeniorCitizenDiscount")
    cb.searchFlight()
    print("Operation is successful")


