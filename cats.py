import requests
import json
from time import sleep
import random


def getMisi(toke):
    url = 'https://cats.garden/api/mission/doneMissionPlatBoot'
    reqhead = {
        'accept': 'application/json',
        'language': 'en', #cadanganmaulana
        'token': toke,
        'Content-Type': 'application/json',
        'Content-Length': '55',
        'Host': 'cats.garden',
        'Connection': 'close',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'okhttp/4.4.0'}
    reqpay = {"missionIds":["61318467-ca27-40ee-abf0-a859424bc1f2"]}
    try:
        r = requests.post(url, data=json.dumps(reqpay), headers=reqhead).json()
        result = r['data']['videoVOList'][0]['userMissionId']
        return result
    except:
    	print("---getMisi Error---")

def exeMisi(misD, toke):
    url = 'https://cats.garden/api/mission/doneMission/{}'.format(misD)
    reqhead = {
        'accept': 'application/json',
        'language': 'en',
        'token': toke,
        'Content-Type': 'application/json',
        'Host': 'cats.garden',
        'Connection': 'close',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'okhttp/4.4.0'}
    reqpay = {}
    try:
        r = requests.post(url, data=json.dumps(reqpay), headers=reqhead).json()
        result = r['data']['coincCarry']
        return result
    except:
    	print("---exeMisi Error---")

def cekSaldo(toke):
    url = 'https://cats.garden/api/cat/refreshState'
    reqhead = {
        'accept': 'application/json',
        'language': 'en',
        'token': toke,
        'Content-Type': 'application/json',
        'Host': 'cats.garden',
        'Connection': 'close',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'okhttp/4.4.0'}
    try:
        r = requests.get(url, headers=reqhead).json()
        result = r['data']
        return result
    except:
    	print("---cekSaldo Error---")


def getGold(toke):
    url = 'https://cats.garden/api/cat/takeAlmsADPrize'
    reqhead = {
        'accept': 'application/json',
        'language': 'en',
        'token': toke,
        'Content-Type': 'application/json',
        'Host': 'cats.garden',
        'Connection': 'close',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'okhttp/4.4.0'}
    reqpay = {}
    try:
        r = requests.post(url, data=json.dumps(reqpay), headers=reqhead).json()
        result = r
        return result
    except:
    	print("---getGold Error---")

token = '2639199e-f24e-45ba-b1ab-5770c15fe40f'
for x in range(1):
	try:
		print(cekSaldo(token))
		print(" ")
		sleep(5)
		misiID = getMisi(token)
		print("Misi : {}".format(misiID))
		print("Coin : {}".format(exeMisi(misiID, token)))
		print(" ")
		sleep(5)
		#print(getGold(token))
		print(" ")
		print("----------Waiting next exe----------")
		print(" ")
		sleep(random.randint(1, 150))
	except:
		break