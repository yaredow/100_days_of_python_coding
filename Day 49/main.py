from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

password = os.environ.get("LINK_PASS")

path = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(executable_path=path)
driver.implicitly_wait(5)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=2882799612&geoId=100212432&keywords=frontend%20developer&location=Ethiopia")
driver.find_element(By.LINK_TEXT, "Sign in").click()
email_address = driver.find_element(By.ID, "username")
email_address.send_keys("yaredyilma11@gmail.com")
pass_word = driver.find_element(By.ID, "password")
pass_word.send_keys("".format(password))
driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()
driver.find_element(By.XPATH, '//*[@id="ember263"]/span').click()
driver.find_element(By.XPATH, '//*[@id="ember300"]/span').click()
driver.find_element(By.XPATH, '//*[@id="ember300"]/span').click()
experience = driver.find_element(By.NAME, 'urn:li:fs_easyApplyFormElement')
experience.send_keys("I have worked on reactJs for almost 4 years")