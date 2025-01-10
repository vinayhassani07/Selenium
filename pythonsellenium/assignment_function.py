import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
lst=[]
driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0
for result in results:
    lst.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click()
print(lst)
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
# time.sleep(5)
prices=driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")

add=0
for price in prices:
    add=add+int(price.text)
print(add)
totalAmount=driver.find_element(By.CSS_SELECTOR, ".totAmt").text
assert add == int(totalAmount)

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait=WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))

text=driver.find_element(By.CLASS_NAME, "promoInfo").text
assert "Code" in text


