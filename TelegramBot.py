import sys

try:
    import requests
    import time
except ModuleNotFoundError as error:
    print(error)
    input("Press Any Key To Exit ...")
    sys.exit()

# Global Variables
api_key = "Write here your API key for bitcoin price"
bot_key = "Write Bot Key here"
chat_id = "Write Chat Id here"
limit = 59000.567988711045
time_interval = 5 * 60


def getBitcoinPrice() -> float:
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    parameters = {
        'start': '1',
        'limit': '2',
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }
    response = requests.get(url=url, headers=headers, params=parameters).json()
    bitcoin_price = float(response["data"][0]["quote"]["USD"]["price"])
    return bitcoin_price


def send_update(msg: str) -> None:
    url = f"https://api.telegram.org/bot{bot_key}/sendMessage"
    parameters = {
        "chat_id": chat_id,
        "text": msg,
    }
    requests.get(url, params=parameters)


def main():
    while True:
        price = getBitcoinPrice()
        print(price)
        if price < limit:
            send_update(msg=f"Bitcoin Price New is {price}")
        time.sleep(5)


if __name__ == '__main__':
    main()
