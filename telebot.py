import datetime, logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

logging.basicConfig(filename="bot.log", level=logging.INFO)

def my_handler(update, context):
    update.message.reply_text("Привет пользователь, сейчас: " + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    # print(update) # Посмотреть что возвращает update

def talk_to_me(update, context):
    text = update.message.text # ввод пользователя
    if text.lower() == "время": 
        text = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")    # если пользователь ввел "время", то выдать текущее дату/время, иначе эхо
    print(text) # вывести сообщение в консоль
    update.message.reply_text(text) # эхо пользователю

def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)
    
    dp=mybot.dispatcher
    dp.add_handler(CommandHandler("start", my_handler))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал " + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

    mybot.start_polling()
    mybot.idle()

main()