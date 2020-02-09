from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import re
import time

driver = webdriver.Chrome()

driver.get("https://patenergy.com/services/patterson-uti-drilling/rig-locator/default.aspx")

csv_file = open('rigs.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)

rows = driver.find_elements_by_xpath('//*[@id="_ctrl0_ctl57_divModuleContainer"]/div/div/div/div[3]/div/ul')

n = 0

for row in rows:

    print('scraping...')

    rig_dict = {}
    
    rig = row.find_element_by_xpath('./li[1]').text
    availability = row.find_element_by_xpath('./li[2]').text
    region = row.find_element_by_xpath('./li[3]').text
    county = row.find_element_by_xpath('./li[4]').text
    horsepower = row.find_element_by_xpath('./li[5]').text
    rig_class = row.find_element_by_xpath('./li[6]').text

    rig_dict['rig'] = rig
    rig_dict['availability'] = availability
    rig_dict['region'] = region
    rig_dict['county'] = county
    rig_dict['horsepower'] = horsepower
    rig_dict['rig_class'] = rig_class

    writer.writerow(rig_dict.values())

    n += 1
    print(n)

    # if n >= 217:
    #     break

print("The scrape is complete.")

csv_file.close()
driver.close()