from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://sotcconnect.travelexic.com/login")
driver.implicitly_wait(5)
email_input = driver.find_element(by="css selector", value="input[name='email']")
email_input.send_keys("aayushi.travelexic@gmail.com")
driver.find_element(by="name", value="password").send_keys("123456")
driver.find_element(by="css selector",value=".btn-primary").click()
driver.implicitly_wait(5)
driver.get("https://sotcconnect.travelexic.com/groups/create")
driver.find_element(by="name",value="driver_pickup_date_time").send_keys("24-11-2023")
# driver.find_element(by="css selector",value="div[name='addtours'] input[placeholder='Select']").click.send_keys("Manali | Shimla")
dropdown_element = driver.find_element(by="css selector",value="div[name='addtours'] input[placeholder='Select']")
target_option_index = 2  # Replace with the index of the option you want to select
for i in range(target_option_index):
        ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
ActionChains(driver).send_keys(Keys.ENTER).perform()