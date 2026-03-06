import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

#Select radio button

wait=WebDriverWait(driver,10)
wait.until(EC.visibility_of_all_elements_located(
    (By.CSS_SELECTOR,"table.tblTrip input")
))
options=driver.find_elements(By.CSS_SELECTOR,"table.tblTrip input")
print(len(options))
for option in options:
    if option.get_attribute("value")=="RoundTrip":
        option.click()
        assert option.is_selected()
        time.sleep(2)
        break

#Checkbox selection

wait.until(EC.visibility_of_all_elements_located(
    (By.CSS_SELECTOR,"#discount-checkbox div input")))
checkboxes=driver.find_elements(By.CSS_SELECTOR, "#discount-checkbox div input")
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("name")=="ctl00$mainContent$chk_SeniorCitizenDiscount":
        checkbox.click()
        time.sleep(2)
        assert checkbox.is_selected()
        break