import logging, sys, datetime
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
        CallbackQueryHandler, ConversationHandler, InlineQueryHandler, ChosenInlineResultHandler)
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telegram.utils.helpers import escape_markdown
from datumbazo import *

def enpaki(bot, update):
    
    kunportajxo = update.message.text.split(' ')[1]
    
    kategorioj = [[KeyboardButton(text='1. Manĝo\nTrinkaĵo')],
                 [KeyboardButton(text='2. Teo')],
                 [KeyboardButton(text='3. Ludo')],
                 [KeyboardButton(text='4. Alia aĵo')]]

    klavaro = ReplyKeyboardMarkup(kategorioj, 
                                  resize_keyboard = False, 
                                  one_time_keyboard = True,
                                  selective = True)

    respondo = update.message.reply_text('Kio estas via kunportaĵo?',
                                         reply_markup = klavaro)
    
    kategorio = respondo.message.text[1]
    
    update.message.reply_text('Via _{kategori}_ *{kunportajx}* estis registrita. Dankon pro via kontribuo!'
                              .format(kategori=kategorio, kunportajx=kunportajxo),
                              parse_mode = ParseMode.MARKDOWN,
                              reply_markup = ReplyKeyboardRemove(remove_keyboard = True, selective = True))

def elpaki(bot, update):
    # print(update)
    update.message.reply_text('Registritaj kunportaĵoj: {afero}'
                              .format(afero=update.message.text.split(' ')[1])
    )

def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)

def main():
    global update_id
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("enpaki", enpaki))
    dp.add_handler(CommandHandler("elpaki", elpaki))
    dp.add_handler(CommandHandler("elpaki", listigi))

    # log all errors
    dp.add_error_handler(error)
    # Start the Bot
    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    if 'genDB' in sys.argv: createDB();
    main()