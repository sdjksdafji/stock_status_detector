import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


'''
return the web element if the item is instock now
'''


def check_bestbuy(driver):
    driver.get("https://www.bestbuy.com/site/nintendo-switch-monster-hunter-rise-deluxe-edition-system-gray-gray/"
               "6454044.p?skuId=6454044")
    # driver.get(
    #     "https://www.bestbuy.com/site/nintendo-switch-32gb-console-neon-red-neon-blue-joy-con/6364255.p?skuId=6364255")
    time.sleep(2.0)
    add_to_cart_buttons = driver.find_elements(By.CLASS_NAME, "add-to-cart-button")
    if len(add_to_cart_buttons) < 1:
        return []

    # suppose to have only one button
    button = add_to_cart_buttons[0]
    text: str = button.text
    if text is not None and text.strip().lower() != "coming soon":
        return [button]

    return []


def check_target(driver):
    driver.get("https://www.target.com/p/nintendo-switch-monster-hunter-rise-deluxe-edition-console/-/A-82493733")
    # driver.get("https://www.target.com/p/toddler-girls-rib-tank-dress-art-class/-/A-81317327?preselect=81641131")
    time.sleep(5.0)
    instock_buttons = []

    pickup_buttons = driver.find_elements(By.XPATH, "//*[@data-test='orderPickupButton']")
    if len(pickup_buttons) > 0:
        for button in pickup_buttons:
            if button.text is not None and "pick" in button.text.strip().lower():
                print("Pickup Available !")
                instock_buttons.append(button)

    deliver_buttons = driver.find_elements(By.XPATH, "//*[@data-test='scheduledDeliveryButton']")
    if len(deliver_buttons) > 0:
        for button in deliver_buttons:
            if button.text is not None and "deliver" in button.text.strip().lower():
                print("Delivery Available !")
                instock_buttons.append(button)

    shipit_buttons = driver.find_elements(By.XPATH, "//*[@data-test='shipItButton']")
    if len(shipit_buttons) > 0:
        for button in shipit_buttons:
            if button.text is not None and "ship" in button.text.strip().lower():
                print("Ship Available !")
                instock_buttons.append(button)

    return instock_buttons


def check_gme(driver):
    driver.get("https://www.gamestop.com/video-games/nintendo-switch/consoles/products/"
               "nintendo-switch-monster-hunter-rise-deluxe-edition/11118957.html?view=new")
    # driver.get("https://www.gamestop.com/video-games/nintendo-switch/consoles/products/"
    #            "nintendo-switch-with-neon-blue-and-neon-red-joy-con/11095819.html?view=new&condition=New")
    time.sleep(2.0)

    instock_buttons = []
    add_to_cart_buttons = driver.find_elements(By.CLASS_NAME, "add-to-cart")
    if len(add_to_cart_buttons) < 1:
        return []

    for button in add_to_cart_buttons:
        text: str = button.text
        if text is not None and text.strip().lower() == "add to cart":
            instock_buttons.append("button")

    return instock_buttons
