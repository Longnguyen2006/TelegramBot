from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
from bs4 import BeautifulSoup

def get_news():
    list_news = []
    r = requests.get('https://www.nbcnews.com/')
    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.find_all("h2", {"class": "tease-card__headline tease-card__title relative"})

    # print(len(mydivs))
    for news in mydivs:
        newdict = {}
        newdict["link"] = news.a.get("href")
        newdict["title"] = news.a.get("title")
        #print(news.a.get("href"))
        list_news.append(newdict)

    return list_news



def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def news(update: Update, context: CallbackContext) -> None:
     data = get_news()
     for item in data:
            update.message.reply_text(f'{item["link"]}')




updater = Updater('5045399918:AAFiASiKPSt0B24socl9_Es557yW3ncPSCo')

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.dispatcher.add_handler(CommandHandler('news', news))

updater.start_polling()
updater.idle()


