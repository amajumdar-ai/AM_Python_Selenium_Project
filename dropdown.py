import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

service_obj=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service_obj)

# #Static Dropdown
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.maximize_window()
# dropdown_list=Select(driver.find_element(By.ID,"dropdown-class-example"))
# time.sleep(2)
# dropdown_list.select_by_value("option1")
# dropdown_list.select_by_index(3)
# time.sleep(2)
# dropdown_list.select_by_visible_text("Option2")
# time.sleep(5)

# Dynamic dropdown
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
wait=WebDriverWait(driver,10)

driver.find_element(By.CSS_SELECTOR, "input[id='autosuggest']").send_keys("us")
wait.until(
    EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, "li.ui-menu-item a")
           )
)
countries=driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "Austria":
        country.click()
        break
time.sleep(5)
assert driver.find_element(By.CSS_SELECTOR, "input[id='autosuggest']").get_attribute("value") == "Austria"
print("Country is selected")

