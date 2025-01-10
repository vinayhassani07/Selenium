import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Vinay")
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
print(alert.text)
assert "Vinay" in alert.text
alert.accept()
# driver.switch_to.window()


time.sleep(2)
