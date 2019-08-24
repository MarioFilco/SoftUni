import requests
import json
import time
from datetime import datetime, timedelta

date = datetime(2018, 1, 10)

for d in range(1, 300 + 1):
    date_ = date - timedelta(days=d)
    date_str = datetime.strftime(date_, "%d-%m-%Y")

    r = requests.get("http://eurofootball.bg/" + date_str + ".json")
    data = r.json()
    date_save = datetime.strftime(date_, "%Y-%m-%d")
    with open('c:/sportmax/' + date_save + '.json', 'w') as f:
        json.dump(data, f)
    print(f"{d} - {date_save}")
    time.sleep(1)


