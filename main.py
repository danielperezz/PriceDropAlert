from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import telebot
import os


def send_telegram_alert(price, url):
    CHAT_ID = os.environ['CHAT_ID']
    TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
    bot = telebot.TeleBot(TELEGRAM_TOKEN)
    msg = "Exiting News! This product price is currently " + \
        str(price) + "₪ Check it out: " + url
    bot.send_message(CHAT_ID, msg)


def check_price(url, desired_price, price_xpath):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, price_xpath)))
        price = float(element.text.strip(" ₪$"))
        if (price < desired_price):
            send_telegram_alert(price, url)
    finally:
        driver.close()


# --------- CHANGE THE VALUES TO ADAPT ---------- #
product_url = r'https://www.terminalx.com/z552090005?color=10'
desired_price = 180
price_xpath = '//*[@id="app-root"]/div[2]/main/div[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/div/div/div'
# ---------------------------------------------- #

display = Display(visible=0, size=(1600, 902))
display.start()
check_price(product_url, desired_price, price_xpath)
