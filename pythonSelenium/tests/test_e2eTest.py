import json

import pytest

from pythonSelenium.pages.loginPage import LoginPage

test_data_path= "./data/test_e2eTest_data.json"
test_data_list=json.load(open(test_data_path))

with open(test_data_path) as f:
    test_data=json.load(f)
    test_data_list=test_data["data"]

@pytest.mark.smoke
@pytest.mark.parametrize("test_data_item",test_data_list)
def test_e2eTest(browserInstance,test_data_item):
    driver=browserInstance
    loginpage=LoginPage(driver)
    print(loginpage.getTitle())
    shopPage=loginpage.loginPage(test_data_item["username"],test_data_item["password"])
    print(shopPage.getTitle())
    shopPage.addItemtoCart(test_data_item["model"])
    checkoutConfirmation=shopPage.click_CheckoutButton()
    checkoutConfirmation.Final_Checkout_Button()
    checkoutConfirmation.country_selection("Ind")
    text=checkoutConfirmation.success_toaster()
    assert "Success" in text








