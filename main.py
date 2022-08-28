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
        price = int(element.text[1:])
        if (price < desired_price):
            send_telegram_alert(price, url)
    finally:
        driver.close()


# --------- CHANGE THE VALUES TO ADAPT ---------- #
product_url = r'https://www.blackandwhiteisrael.co.il/product/%d7%9b%d7%a4%d7%9b%d7%a4%d7%99-%d7%a7%d7%95%d7%9c%d7%95%d7%a8-%d7%9b%d7%a1%d7%a3/'
desired_price = 170
price_xpath = '//*[@id="product-1265711"]/div[1]/div[2]/div/div/div[2]/div/p/ins/span'
# ---------------------------------------------- #

display = Display(visible=0, size=(1600, 902))
display.start()
check_price(product_url, desired_price, price_xpath)
