from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
from bs4 import BeautifulSoup


def get_news():
    list_news = []
    r = requests.get("https://baotintuc.vn/tags/nga.htm")
    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.find_all("h3", {"class": "des"})

    for new in mydivs:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_news.append(newdict)

    return list_news


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'xin chao {update.effective_user.first_name}')


def news(update: Update, context: CallbackContext) -> None:
    data = get_news()
    str1 = " "

    for item in data:
        str1 += item["title"] + "\n"
    update.message.reply_text(f'{str1}')



updater = Updater('5045399918:AAFiASiKPSt0B24socl9_Es557yW3ncPSCo')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('news', news))

updater.start_polling()
updater.idle()