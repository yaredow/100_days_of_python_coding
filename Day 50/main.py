from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

path = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(executable_path=path)
driver.get("https://tinder.com/app/recs")
sleep(3)
driver.find_element(By.XPATH, '//*[@id="t-48487324"]/div/div[2]/div/div/div[1]/button').click()
login = driver.find_element(By.XPATH, '//*[@id="t-48487324"]/div/div[1]/div/main/div['
                                         '1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()
sleep(2)
fb_login = driver.find_element(By.XPATH, '//*[@id="t-1776868400"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()
sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
email = driver.find_element(By.NAME, "email")
email.send_keys("yaredyilma11@gmail.com")
password = driver.find_element(By.NAME, "pass")
password.send_keys("dopellex11")
driver.find_element(By.NAME, "login").click()
# allow notification
driver.implicitly_wait(4)
allow_notification = driver.find_element(By.XPATH, '//*[@id="t-1776868400"]/div/div/div/div/div[3]/button[1]')
allow_notification.click()
# allow location
allow_location = driver.find_element(By.XPATH, '//*[@id="t-1776868400"]/div/div/div/div/div[3]/button[1]')
allow_location.click()
# like people

print(driver.title)