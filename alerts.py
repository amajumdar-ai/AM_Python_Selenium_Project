import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
name="Arpita"
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@placeholder='Enter Your Name']").send_keys(name)
driver.find_element(By.CSS_SELECTOR,"#alertbtn").click()
alert=driver.switch_to.alert
altertext=alert.text
print(altertext)
assert name in altertext
print(f"{name} is present in the alert")
alert.accept()
time.sleep(2)