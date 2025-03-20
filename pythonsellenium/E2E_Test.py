import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(5)
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
products=driver.find_elements(By.CSS_SELECTOR, "div[class='card h-100']")

for product in products:
    product_name=product.find_element(By.CSS_SELECTOR, "div h4.card-title a").text
    if product_name == "Blackberry":
        product.find_element(By.CSS_SELECTOR, "div button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

driver.find_element(By.XPATH, "//button[@class= 'btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("ind")
wait=WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "input[type='submit'").click()
msg=driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Success" in msg
driver.close()

