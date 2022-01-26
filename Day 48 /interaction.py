from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

path = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(executable_path=path)
driver.get("http://secure-retreat-92358.herokuapp.com/")
user_name = driver.find_element(By.NAME, "fName")
user_name.send_keys("Yared")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Yilma")
email = driver.find_element(By.NAME, "email")
email.send_keys("yaredyilma11@gmail.com")
submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()