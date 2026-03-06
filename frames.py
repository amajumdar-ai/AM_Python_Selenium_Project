import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.switch_to.frame("courses-iframe")
driver.find_element(By.XPATH,"//ul[@class='navigation clearfix']/li[7]").click()
time.sleep(2)
print(driver.find_element(By.CSS_SELECTOR,"h2").text)
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"h1").text)
time.sleep(2)