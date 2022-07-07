from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler,Filters
import os
TOKEN=os.environ.get("TELEGRAM_ID")
def start(update,context):
    yourname=update.message.chat.first_name
    msg="Hi"+yourname+"! Welcome to Lingua Franca Vocab Bot"
    context.bot.send_message(update.message.chat.id,msg)

def mimic(update,context):
    context.bot.send_message(update.message.chat.id,update.message.text)

def details(update,context):
    context.bot.send_message(update.message.chat.id,update.message.text)

def error(update,context):
    context.bot.send_message(update.message.chat.it, "OOps! Error encountered")

def main():
    updater=Updater(token=TOKEN)   #updater
    dp=updater.dispatcher          #dispatcher

    ###################   Handlers :
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("details", details))

    dp.add_handler(MessageHandler(Filters.text,mimic))

    dp.add_error_handler(error)

    #updater.start_polling()
    updater.start_webhook(listen="0.0.0.0",
                          port=os.environ.get("PORT",443),
                          url_path=TOKEN,
                          webhook_url="https://lingu-bot.herokuapp.com/"+TOKEN
                          )

    updater.idle()

if __name__=='__main__':
    main()
