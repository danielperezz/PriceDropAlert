from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display
from selenium.webdriver.chrome.options import Options
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
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


# def send_whatsapp_alert(price, url):
#     wtp_url = "https://web.whatsapp.com/send?phone=+972503493335"
#     msg = "Exiting News! This product price is currently " + \
#         str(price) + "₪ Check it out: " + url
#     # options = Options()
#     # options.add_argument(
#     #     r"user-data-dir=whatsapp_profile")

#     # options.add_argument("profile-directory=whatsapp_profile")
#     wtp_driver = webdriver.Chrome(
#         service=Service(ChromeDriverManager().install()))
#     wtp_driver.get(wtp_url)
#     try:
#         typebox = WebDriverWait(wtp_driver, 20).until(
#             EC.presence_of_element_located((By.XPATH, r'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')))
#         time.sleep(3)
#         typebox.send_keys(msg)
#         time.sleep(3)
#         typebox.send_keys(Keys.ENTER)
#         time.sleep(3)
#     finally:
#         wtp_driver.close()


def check_price():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    url = r'https://www.blackandwhiteisrael.co.il/product/%d7%9b%d7%a4%d7%9b%d7%a4%d7%99-%d7%a7%d7%95%d7%9c%d7%95%d7%a8-%d7%9b%d7%a1%d7%a3/'
    driver.get(url)

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="product-1265711"]/div[1]/div[2]/div/div/div[2]/div/p/ins/span')))
        price = int(element.text[1:])
        if (price < 170):
            send_telegram_alert(price, url)
    finally:
        driver.close()


display = Display(visible=0, size=(1600, 902))
display.start()
check_price()
