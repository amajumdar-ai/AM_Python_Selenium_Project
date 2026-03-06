import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://the-internet.herokuapp.com/windows")
# driver.maximize_window()
# driver.find_element(By.LINK_TEXT,"Click Here").click()
# window_handle = driver.window_handles # to handle multiple windows and perform actions
# driver.switch_to.window(window_handle[1])
# print(driver.find_element(By.CSS_SELECTOR,"h3").text)
# driver.close()
# driver.switch_to.window(window_handle[0])
# print(driver.find_element(By.CSS_SELECTOR,"h3").text)
wait=WebDriverWait(driver,10)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
# wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".im-para.red")))
text = driver.find_element(By.XPATH, "//p[@class='im-para red']").text
print(text)
splitted_text=text.split()

for text in splitted_text:
    if "@" in text:
        email=text.strip(".,?")
        break
print(email)
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.ID,"password").send_keys("123")
driver.find_element(By.ID,"terms").click()
options=Select(driver.find_element(By.XPATH,"//select[@class='form-control']"))
options.select_by_value("teach")
driver.find_element(By.ID,"signInBtn").click()
time.sleep(2)
alter_text=driver.find_element(By.XPATH,"//div[@class='alert alert-danger col-md-12']").text
print(alter_text)

time.sleep(2)

