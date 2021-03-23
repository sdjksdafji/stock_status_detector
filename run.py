from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

from detect.mh_rise import check_bestbuy, check_target, check_gme

fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.headless = True
with webdriver.Firefox(firefox_options=fireFoxOptions) as driver:
    print(check_bestbuy(driver))
    print(check_target(driver))
    print(check_gme(driver))
