from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas
chrome_driver_path = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org/")
event_time = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}
for n in range(len(event_names)):
    events[n] = {
        "time": event_time[n].text,
        "name": event_names[n].text,
    }
print(events)
events_csv = pandas.DataFrame("events.csv")
driver.quit()