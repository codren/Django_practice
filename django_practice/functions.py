import requests, datetime

def get_exchange():
    today = datetime.datetime.now()
    if today.weekday() >= 5:
        diff = today.weekday()-4
        today = today - datetime.timedelta(days=diff)

    today = today.strftime('%Y%m%d')
    auth = 'dTT5WZksqNwVrZgBL6XfhRR96Df6FRPz'
    url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={}&searchdate={}&data=AP01'
    url = url.format(auth, today)

    res = requests.get(url)
    data = res.json()

    for d in data:
        if d['cur_unit'] == 'USD':
            return d['tts']
    return
