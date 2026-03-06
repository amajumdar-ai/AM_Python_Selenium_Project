from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


service_obj=Service(ChromeDriverManager().install())
driver= webdriver.Chrome(service=service_obj)
wait= WebDriverWait(driver,10)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
login_page_url=driver.current_url
driver.find_elements(By.CSS_SELECTOR,".form-control")[0].send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Learning@830$3mK2")
dropdown=Select(driver.find_element(By.XPATH, "//select[@class='form-control']"))
dropdown.select_by_index(1)
driver.find_element(By.ID, 'terms').click()
driver.find_element(By.XPATH, "//input[@id='signInBtn']").click()


wait.until(EC.url_changes(login_page_url))
homepage_url=driver.current_url
assert homepage_url!=login_page_url, \
    "Login failed url did not match"
print("Login Successful")


# wait.until(
#     EC.text_to_be_present_in_element(
#         (By.XPATH, "//form[@id='login-form']//div[contains(@class,'alert-danger')]"),
#         "Incorrect"
#     )
# )
# 
#
# error_banner=driver.find_element(By.XPATH, "//form[@id='login-form']//div[contains(@class,'alert-danger')]")
# actual_text=error_banner.text
# print("Actual text is:", actual_text)
# assert "Incorrect username/password." in actual_text
# print("Login failed message displayed correctly")

time.sleep(5)


driver.close()

time.sleep(5)