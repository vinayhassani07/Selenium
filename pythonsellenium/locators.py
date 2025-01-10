import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.find_element(By.NAME, "email").send_keys("heloo@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456789")
driver.find_element(By.ID, "exampleCheck1").click()
dropdown= Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(1)
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "successfully" in message
driver.find_element(By.CSS_SELECTOR, "input[name='name'").send_keys("Vinay")
time.sleep(2)
