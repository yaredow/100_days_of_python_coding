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
fb_login = driver.find_element(By.XPATH, '//*[@id="t-1776868400"]/div/div/div[1]/div/div[3]/span/div[2]/button/')
fb_login.click()
sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)