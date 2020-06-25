import logging
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, Filters
from telegram.utils.helpers import escape_markdown
from skcheck import skcheck


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! \n\n')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text("Sorry can't help you 🙂")



def main():
    updater = Updater("1224271943:AAHdX4Ew6C-55QSuka2qg6CCP5LsIPhC8_s", use_context=True)
    
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("sk", skcheck))
    #dp.add_handler(CommandHandler("allindodax", indodax))
    


    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()