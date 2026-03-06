import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(10)

# css= a[href*='shop'] xpath=//a[contains(@href, 'shop')]

driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='card h-100']")))
mobiles=driver.find_elements(By.XPATH,"//div[@class='card h-100']")
print(len(mobiles))
model_names=[]
for mobile in mobiles:
    model=mobile.find_element(By.XPATH,".//h4/a").text
    driver.execute_script("window.scrollTo(0,3000)")
    if model=='Blackberry':
        mobile.find_element(By.XPATH,".//button[text()='Add ']").click()
driver.execute_script("window.scrollTo(0,10)")
button_text=driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").text
print(button_text)
driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
total_price=driver.find_element(By.XPATH,"//tr[2]/td[5]/h3").text
print(total_price)

driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("IN")
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_all_elements_located((By.CSS_SELECTOR,"div.suggestions li a")))
countries=driver.find_elements(By.CSS_SELECTOR,"div.suggestions li a")
print(len(countries))
for country in countries:
    if country.text=="India":
        country.click()
        break
driver.find_element(By.CSS_SELECTOR,".checkbox.checkbox-primary").click()
driver.find_element(By.XPATH,"//input[@value='Purchase']").click()
time.sleep(2)
success_toaster=driver.find_element(By.CSS_SELECTOR,".alert.alert-success.alert-dismissible").text
print(success_toaster)
assert "Success" in success_toaster
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,".alert.alert-success.alert-dismissible a").click()
assert "Success" in success_toaster
time.sleep(5)