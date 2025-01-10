import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# If the chrome driver dosent work  then this code
# service=Service("E:/vinay/Automation/Selenium - 2025/chromedriver-win64/chromedriver.exe")
# driver=webdriver.Chrome(service=service)
# driver.get("https://rahulshettyacademy.com")

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
time.sleep(2)
