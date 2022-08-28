# PriceDropAlert

## Description:
A python script to check the price of a product and send a telegram message if it's lower then a certain number

## How to Use:
* Change the `product_url` variable to the url of the desired product
* Change the `desired_price`
* Change the `price_xpath` to the xpath of the price html element (get it by inspecting the webpage, then tracking the price element, then right click on it's code block > copy xpath)
* In your github repo, add two secrets: 
  * `CHAT_ID` for your bot chat id
  * `TELEGRAM_TOKEN` for yout bot secret token
  * You can get them both using [this tutorial](https://medium.com/cocoaacademymag/how-to-integrate-github-actions-with-slack-telegram-and-whatsapp-67a4dca0f17d#:~:text=Integrating%20with%20Telegram) 
 * The script is scheduled to run everyday at 8am. To change it edit the the `schedule` section inside the `.yml` file with the desired schedule in cron sytax ([recommended generator](https://crontab-generator.org/) to produce a crontab syntax)
