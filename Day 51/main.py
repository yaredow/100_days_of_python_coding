from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from time import sleep

CHROME_DRIVER_PATH = "/usr/local/bin/chromedriver"
INTERNET_SPEED = 3


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://fast.com/")
        sleep(30)
        self.up = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[2]/div/div[1]').text
        print(self.up)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/home")
        sleep(4)
        google_sign_in = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div['
                                                            '1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                                            '2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
        google_sign_in.send_keys("yaredyilma2020@outlook.com")
        next_button = self.driver.find_element(By.XPATH,
                                               '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div['
                                               '2]/div/div/div[2]/div[2]/div[1]/div/div[6]')
        next_button.click()
        sleep(2)

        username = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div['
                                                      '2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div['
                                                      '2]/label/div/div[2]/div/input')
        username.send_keys("@yaredow")
        another_next_button = self.driver.find_element(By.XPATH,
                                                       '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div['
                                                       '2]/div/div/div[2]/div[2]/div[2]/div/div')
        another_next_button.click()
        sleep(3)
        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                      '2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div['
                                                      '2]/div[1]/input')
        password.send_keys("dopellex11")
        log_in = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div['
                                                    '2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div')
        log_in.click()
        sleep(8)
        post = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div['
                                                  '2]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                                  '1]/div/div/div/div/div/div/div/div/div/label/div['
                                                  '1]/div/div/div/div/div[2]/div/div/div/div')
        post_text = f"@ethiotelecom, Why is my internet speed {self.up}mb/s when I pay for {INTERNET_SPEED}mb/s?"
        post.send_keys(post_text)
        post = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div['
                                                  '2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div['
                                                  '3]')
        post.click()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
