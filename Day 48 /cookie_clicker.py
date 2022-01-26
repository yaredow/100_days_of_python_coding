from selenium import webdriver
from selenium.webdriver.common.by import By
import time

path = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(executable_path=path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")
# get upgrade item ids
item = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [data.get_attribute("id")for data in item]

time_out = time.time() + 5
five_minute = time.time() + 5*60

while True:
    # cookie.click()
    if time.time() > time_out:
        all_prices = []
        prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        for price in prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                all_prices.append(cost)
        cookie_upgrades = {}
        for n in range(len(all_prices)):
            cookie_upgrades[all_prices[n]] = item_ids[n]

        # get current cookie
        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element.replace(",", "")
        cookie_count = int(money_element)
        # find upgrade
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id
        # purchase the most afordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
        driver.find_element(By.ID, to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

        # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_minute:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break
