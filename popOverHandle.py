import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
action=ActionChains(driver) #to perform browser actions
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
time.sleep(2)
action.move_to_element(driver.find_element(By.LINK_TEXT,"Top")).click().perform()
time.sleep(2)

