import os
import time

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from twilio.rest import Client

from detect.mh_rise import check_bestbuy, check_target, check_gme


def notify_phone(number):
    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)

    client.calls.create(
        url='http://demo.twilio.com/docs/voice.xml',
        to=number,
        from_='+17342704043'
    )


def check_stock_status():
    options = Options()
    options.headless = True
    useragent = UserAgent(verify_ssl=False)
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", useragent.random)

    is_instock = False

    with webdriver.Firefox(firefox_profile=profile, options=options) as driver:
        best_buy_result = check_bestbuy(driver)
        target_result = check_target(driver)
        gme_result = check_gme(driver)

    if len(best_buy_result) > 0:
        print("Best buy in stock !!!!!!!!!!!!!!!!!!")
        is_instock = True

    if len(target_result) > 0:
        print("Target in stock !!!!!!!!!!!!!!!!!!")
        is_instock = True

    if len(gme_result) > 0:
        print("GameStop in stock !!!!!!!!!!!!!!!!!!")
        is_instock = True

    return is_instock


stock_counter = 0


def check_and_call():
    global stock_counter
    if check_stock_status():
        stock_counter += 1
    else:
        stock_counter = 0

    if stock_counter >= 3:
        notify_phone("+16073791828")


if __name__ == "__main__":
    while True:
        try:
            for i in range(100):
                check_and_call()
                time.sleep(10)
            print("No stock found so far. Checking again...")
        except KeyboardInterrupt:
            print("KeyboardInterrupt")
            break
        except Exception:
            print("Exception happened")
