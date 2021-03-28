from requests import Session
import requests
from threading import Thread

request = Session()

proxies = open("proxy.txt", "r").read().strip().splitlines()

url = "https://www.instagram.com/accounts/login/ajax/"

data = {
    "username": "sdfjlksjflk",
    "enc_password": "#PWD_INSTAGRAM_BROWSER:10:1609186862:ATJQAIA51VP70wNz2Hrh5DtFXyfwFIj3lae8Jo4Awqj5fYYheYmpa3b3CakjfF0hHSsF6MFIKE7Ylg5K0nXN7IHh9WWNUteFhYt0zOxwa7omE7MQOSvBd+lr6V/IRzolaw/gTrhxFvRz4xXWqg==",
    "queryParams": "{}",
    "optIntoOneTap": "false"
}

headers = {

    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "ar,en-US;q=0.9,en;q=0.8",
    "content-length": "276",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://www.instagram.com",
    "referer": "https://www.instagram.com/accounts/login/",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "x-csrftoken": "Zl0HtY9MxBRBBM4CuDJM53xrmXivLaos",
    "x-ig-app-id": "936619743392459",
    "x-ig-www-claim": "hmac.AR3Et8wKm2CQpY0t5wZtsXmBfKDBEU1Dl03qPrS7v-Fedd8h",
    "x-instagram-ajax": "b10813bd9030",
    "x-requested-with": "XMLHttpRequest"
}


def PorxyChecker():
    for proxy_ in proxies:
        poxy = {
            "https": f"https://{proxy_}",
            "http": f"http://{proxy_}"
        }
        try:
            request.post(url, data=data, headers=headers, proxies=poxy)
        except requests.exceptions.ConnectionError:
            print(f"bad proxy: {proxy_}")
        else:
            print(f"good proxy: {proxy_}")
            with open("GoodProxy.txt", mode="w") as p:
                p.write(proxy_ + "\n")


for i in range(50):
    Thread(target=PorxyChecker).start()
