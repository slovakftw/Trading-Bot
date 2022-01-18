import requests
import json

# i think this is the moving avg
base_url = "https://api.oceanex.pro/v1"


def barshistory():
    method_url = base_url + "/k"
    data = {
        'market': 'vetusdt',
        # # of data points
        'limit': 18,
        # period in mins
        'period': 60,
        # 'timestamp': 160928700,
    }
    r = requests.post(method_url, data=data)
    bardata = (json.loads(r.text))['data']
    open = []
    high = []
    low = []
    close = []
    volume = []
    for i in (bardata):
        open.append(i[1])
        high.append(i[2])
        low.append(i[3])
        close.append(i[4])
        volume.append(i[5])
    print(bardata)
    oavg = sum(float(i) for i in open) / len(open)
    print("open", open, "open avg=", oavg)
    havg = sum(float(i) for i in high) / len(high)
    print("high", high, "high avg=", havg)
    lavg = sum(float(i) for i in low) / len(low)
    print("low", low, "low avg=", lavg)
    cavg = sum(float(i) for i in close) / len(close)
    print("close", close, "close avg=", cavg)
    vavg = sum(float(i) for i in volume) / len(volume)
    print("Volume", volume, "volume avg=", vavg)


barshistory()
