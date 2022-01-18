import requests
import json


base_url = "https://api.oceanex.pro/v1"


def recentrades():
    method_url = base_url + "/trades"
    market = "vetusdt"
    limit = 20
    # start_time = 1609274232
    # end_time = 1609274309
    # from_id = 1000
    # to_id = 1200000
    data = {
        "market": market,
        "limit": limit,
        # "start": start_time,
        # "end": end_time,
        # "from": from_id,
        # "to": to_id
    }
    r = requests.post(method_url, data=data)
    tdata = (json.loads(r.text))['data']
    print(tdata)
    buylst = []
    selllst = []
    for i in (tdata):
        if i['side'] == ('bid'):
            buylst.append(i['price'])
        if i['side'] == ('ask'):
            selllst.append(i['price'])

    print("buy prices", buylst)
    x = sum(float(i) for i in buylst) / len(buylst)
    print("buy avg =", x)
    print("sell prices", selllst)
    y = sum(float(o) for o in selllst) / len(selllst)
    print("sell avg =", y)


recentrades()
