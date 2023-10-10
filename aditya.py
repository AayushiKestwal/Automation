from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://sotcconnect.travelexic.com/')

time.sleep(5)

email_likh = driver.find_element(By.CSS_SELECTOR, 'input.form-control[type=email]')
email = "adityarai366@gmail.com"
email_likh.send_keys(email)

password_likh = driver.find_element(By.CSS_SELECTOR, 'input.form-control[type=password]')
password = "12345678"
password_likh.send_keys(password)

click_kr = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
click_kr.click()

time.sleep(5)

# driver.quit()
