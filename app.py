from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler

import os
from telegram import Update
from telegram.ext import CallbackContext, ApplicationHandlerStop, TypeHandler, Application
SPECIAL_USERS = [2060060048, 172380183, 1827979793]  # Allows users

TOKEN="5332532839:AAHkaINudmaGOwCMWXW9-IBFqY3ye-SMmeE"
def start(update,context):
    yourname=update.message.chat.first_name
    msg="Hi"+yourname+"! Welcome to Lingua Franca Vocab Bot"
    context.bot.send_message(update.message.chat.id,msg)

def mimic(update,context):
    context.bot.send_message(update.message.chat.id,update.message.text)
def error(update,context):
    context.bot.send_message("oops ! Error aa gya")
def details(update,context):
    context.bot.send_message(update.message.chat.id,update.message.text)

#async def callback(update: Update, context: CallbackContext):
    #"""Handle the update"""
    #await start(update, context)
    #raise ApplicationHandlerStop # Only if you DON'T want other handlers to handle this update

async def callback(update: Update, context: CallbackContext):
    """Handle the update"""
    await start(update, context)
    raise ApplicationHandlerStop # Only if you DON'T want other handlers to handle this update

async def callback(update: Update, context: CallbackContext):
    if update.effective_user.user_id in SPECIAL_USERS:
        pass
    else:
        await update.effective_message.reply_text("Hey! You are not allowed to use me!")
        raise ApplicationHandlerStop

app = Application.builder().token("TOKEN").build()
handler = TypeHandler(Update, callback) # Making a handler for the type Update
app.add_handler(handler, -1) # Default is 0, so we are giving it a number below 0
# Add other handlers and start your bot.

updater=Updater(token=TOKEN)   #updater
dp=updater.dispatcher          #dispatcher

    ###################   Handlers :
dp.add_handler(CommandHandler("start",start))
dp.add_handler(CommandHandler("details", details))



dp.add_error_handler(error)
app = Application.builder().token("TOKEN").build()
handler = TypeHandler(Update, callback) # Making a handler for the type Update
app.add_handler(handler, -1) # Default is 0, so we are giving it a number below 0
# Add other handlers and start your bot.
    #updater.start_polling()
updater.start_webhook(listen="0.0.0.0",
                          port=os.environ.get("PORT",443),
                          url_path=TOKEN,
                          webhook_url="https://lingu-bot.herokuapp.com/"+TOKEN
                          )

updater.idle()


