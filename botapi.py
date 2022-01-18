import requests
import json
import pandas as pd


base_url = "https://api.oceanex.pro/v1"

# markets avaiable to trade on. status update


def marketupdate():
    method_url = base_url + "/markets"
    r = requests.post(method_url)
    print(r)
    print(r.text)
    print("market")
    print(r)

# Oceanex time


def Servertime():
    method_url = base_url + "/timestamp"
    r = requests.post(method_url)
    print(r.text)
    print("here")


# last trade (tick), best bid/ask and volume.


def Lasttrade():
    market = "vetusdt"
    method_url = base_url + "/tickers/{}".format(str(market))
    r = requests.post(method_url, timeout=5)
    print(r)
    print(r.text)


Servertime()
Lasttrade()


# tickers multiple
# method_url = base_url + "/tickers_multi"
# markets = ["vetusdt", "vetbtc"]
# data = {
#    "markets[]": markets
# }
# r = requests.post(method_url, data=data)
# print("hello")
# print(r.text)
