import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
lst=[]
driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

veggieWeb_element=driver.find_elements(By.XPATH, "//tr/td[1]")
for element in veggieWeb_element:
    lst.append(element.text)

original=lst.copy()
lst.sort()

assert lst == original
