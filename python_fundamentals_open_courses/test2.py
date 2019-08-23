import requests
import json
from datetime import datetime, timedelta, date
import time

# path = 'c:/21-08-2019.json'
# with open(path) as json_file:
#     sportmax_results = json.load(json_file)
date = datetime(2019, 8, 22)
# print(date_)
# print(type(date_))
# print()
for d in range(1, 125):

    date_ = date - timedelta(days=d)
    date_str = datetime.strftime(date_, "%d-%m-%Y")
    # print(date_str)
    # print(type(date_str))
    # print()
    r = requests.get("http://eurofootball.bg/" + date_str + ".json")
    sportmax_results = json.loads(r.text)


    data = r.json()
    with open('c:/sportmax/' + date_str + '.json', 'w') as f:
        json.dump(data, f)



    # results = markets['markets']['6']['odds']
    for i in sportmax_results.items():
        # print(i[1]['markets']['6']['odds'])
        search_ = i[1]['markets']['6']['odds']
        for s in search_.items():
            if s[0] == '90с - 120с' and 'W41.14' in s[1]:
                print("-----------")
                print(date_str)
                print("-----------")
                print(s)
                print(i)
                print()
    time.sleep(1)
    # print(d)

# print(sportmax_results)


# r = requests.get("https://poloniex.com/public?command=returnOrderBook&currencyPair=USDT_BTC&depth=10")
# usdt_btc = json.loads(r.text)
# r = requests.get("https://poloniex.com/public?command=returnOrderBook&currencyPair=USDT_DOGE&depth=10")
# usdt_doge = json.loads(r.text)
# r = requests.get("https://poloniex.com/public?command=returnOrderBook&currencyPair=BTC_DOGE&depth=10")
# btc_doge = json.loads(r.text)
# usdt_btc_asks = usdt_btc['asks'][0]
# usdt_btc_bids = usdt_btc['bids'][0]
# usdt_doge_asks = usdt_doge['asks'][0]
# usdt_doge_bids = usdt_doge['bids'][0]
# btc_doge_asks = btc_doge['asks'][0]
# btc_doge_bids = btc_doge['bids'][0]
# print(f"USDT_BTC{usdt_btc_asks} <-> {usdt_btc_bids}")
# print(f"USDT_DOGE{usdt_doge_asks} <-> {usdt_doge_bids}")
# print(f"BTC_DOGE{btc_doge_asks} <-> {btc_doge_bids}")
# btc_money = 1
#
# result = btc_money * float(usdt_btc_bids[0])
# result = result / float(usdt_doge_asks[0])
# result = result * float(btc_doge_bids[0])
# print()
# print(f"{btc_money} -> {result:.4f} -> {result - btc_money:.4f} ->> {(result - btc_money)*float(usdt_btc_bids[0]):.2f} USD")
#
#
# doge_money = btc_money / float(btc_doge_asks[0])
#
# result_1 = doge_money * float(btc_doge_bids[0])
# result_1 = result_1 * float(usdt_btc_bids[0])
# result_1 = result_1 / float(usdt_doge_asks[0])
# print()
# print(f"{doge_money} -> {result_1:.4f} -> {result_1 - doge_money:.4f} ->> {(result_1 - doge_money)*float(usdt_doge_bids[0]):.2f} USD")
#
#
# usdt_money = btc_money * float(usdt_btc_bids[0])
#
# result_2 = usdt_money / float(usdt_doge_asks[0])
# result_2 = result_2 * float(btc_doge_bids[0])
# result_2 = result_2 * float(usdt_btc_bids[0])
# print()
# print(f"{usdt_money} -> {result_2:.4f} -> {result_2 - usdt_money:.4f} ->> {(result_2 - usdt_money):.2f} USD")
