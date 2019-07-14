import logging, sys, datetime
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
        CallbackQueryHandler, ConversationHandler, InlineQueryHandler, ChosenInlineResultHandler)
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent
from telegram.utils.helpers import escape_markdown
from datumbazo import *

def kunporti_ludon():
    pass

def kunporti_teon():
    pass

def elpacki():
    pass

def main():
    global update_id
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("YOUR_TELEGRAM_API_KEY")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("ludo", kunporti_ludon))
    dp.add_handler(CommandHandler("teo", kunporti_teon))
    dp.add_handler(CommandHandler("elpaki", elpacki))

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
