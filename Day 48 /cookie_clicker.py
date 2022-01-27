from selenium import webdriver
from selenium.webdriver.common.by import By
import time

path = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(executable_path=path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
# get cookie to click on
cookie = driver.find_element(By.ID, "cookie")
# finding the upgrade id
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
items_id = [item.get_attribute("id") for item in items]
# time out
timeout = time.time() + 5
five_min = time.time() + 5*60

while True:
    cookie.click()
    # every 5 seconds
    if time.time() > timeout:
        # get all the upgrades
        prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []
        for price in prices:
            elements_text = price.text
            if elements_text != "":
                cost = int(elements_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)
        # create a dictionary of store item and price
        cookie_upgrade = {}
        for n in range(len(item_prices)):
            cookie_upgrade[item_prices[n]] = items_id[n]
        # current cookie count
        current_money = driver.find_element(By.ID, "money").text
        if "," in current_money:
            current_money = current_money.replace(",", "")
        cookie_count = int(current_money)
        # find affordable upgrades
        affordable_upgrade = {}
        for cost, iid in cookie_upgrade.items():
            if cookie_count > cost:
                affordable_upgrade[cost] = iid

        # The most expensive upgrade
        highest_affordable_upgrade = max(affordable_upgrade)
        print(highest_affordable_upgrade)
        purchase_id = affordable_upgrade[highest_affordable_upgrade]
        driver.find_element(By.ID, purchase_id).click()
        # add another 5 seconds
        timeout = time.time() + 5
        # after 5 minutes stop the bot
        if time.time() > five_min:
            cookie_per_second = driver.find_element(By.ID, "cps").text
            print(cookie_per_second)
            break



