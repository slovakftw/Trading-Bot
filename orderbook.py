import requests
import pandas as pd
import json
import numpy as np

base_url = "https://api.oceanex.pro/v1"


def orderbk(base_url):
    market = "vetusdt"
    limit = 5
    method_url = base_url + "/order_book"
    data = {"market": market, "limit": limit}
    r = requests.post(method_url, data=data)
    print(r.text)
    tdata = (json.loads(r.text))['data']['asks']
    print("asks. price with volume")
    for i in (tdata):
        print(i)
        print(i[0])
    print("bids. price with volume")
    for i in (tdata):
        print(i)
        print(i[0])


orderbk(base_url)
# method_url = base_url + "/order_book/multi"
# markets = ["vetusdt", "vetbtc"]
# limit = 5
# data = {
#     "markets[]": markets,
#     "limit": limit
# }
# r = requests.post(method_url, data=data)
# print(r.text)
