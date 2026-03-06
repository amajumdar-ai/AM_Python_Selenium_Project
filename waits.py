import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
wait=WebDriverWait(driver,10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
expected_list=['Cucumber','Raspberry','Strawberry']
driver.find_element(By.CSS_SELECTOR,"input.search-keyword").send_keys("ber")
wait.until(lambda d: len(
    d.find_elements(By.XPATH, "//div[@class='products']/div")
) == 3)
total=driver.find_elements(By.XPATH,"//div[@class='products']/div")
vegetables_names=driver.find_elements(By.CSS_SELECTOR, "div div h4")
actual_list=[]
for vegetable in vegetables_names:
    names=vegetable.text.split("-")[0].strip()
    actual_list.append(names)
assert actual_list==expected_list
print("veggies are present")







count=len(total)
print(count)

for item in total:
    item.find_element(By.XPATH,"div/button").click()
driver.find_element(By.CSS_SELECTOR,"a.cart-icon").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
wait.until(EC.visibility_of_all_elements_located(
    (By.XPATH,"//td[5]/p")
              ))


prices = driver.find_elements(By.XPATH, "//td[5]/p")
sum=0
for price in prices:
    sum+=int(price.text)
print(sum)
total_amount=int(driver.find_element(By.CSS_SELECTOR,"span.totAmt").text)
print(total_amount)
assert sum==total_amount
print("sum of products are correct ")
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".promoCode")))
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR,".promoInfo"))
)
prom_info=driver.find_element(By.CSS_SELECTOR,".promoInfo")
print(prom_info.text)
Total_After_Discount=float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
print(Total_After_Discount)
assert Total_After_Discount<total_amount
time.sleep(2)
