try:
    import requests, uuid, secrets
    from time import sleep
except ModuleNotFoundError as e:
    import sys

    print(e)
    input("Enter to exit..")
    sys.exit()

uid = uuid.uuid4()
session = requests.Session()

cookie = secrets.token_hex(8) * 2
username = input("USER>>")
password = input("PASSWORD>>")
target = input("TARGET>>")
sleep_time = int(input("SLEEP>>"))
done_spam = 1
error_spam = 1


def login():
    url = "https://www.instagram.com/accounts/login/ajax/"
    data = {

        "username": username,
        "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:1609186862:{password}",
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
        "x-csrftoken": "missing",
        "x-ig-app-id": "936619743392459",
        "x-ig-www-claim": "hmac.AR3Et8wKm2CQpY0t5wZtsXmBfKDBEU1Dl03qPrS7v-Fedd8h",
        "x-instagram-ajax": "b10813bd9030",
        "x-requested-with": "XMLHttpRequest",
        "mid": cookie
    }
    res_login = session.post(url, headers=headers, data=data, allow_redirects=True)
    if res_login.json()["authenticated"] == True:
        print(f"[√] LOGIN DONE :{username}")
        print("\n")
        session.headers.update({'X-CSRFToken': res_login.cookies['csrftoken']})
        instagram_spam()
    else:
        print(f"[x] ERROR LOGIN :{username}")


def instagram_spam():
    global done_spam
    global error_spam
    url_id = f"https://www.instagram.com/{target}/?__a=1"
    res_id = session.get(url_id).json()
    user_id = str(res_id["logging_page_id"])
    idd = user_id.split("_")[1]
    while True:
        urlrep = f"https://i.instagram.com/users/{idd}/report/"
        data_spam = {
            'source_name': '', 'reason_id': 1, 'frx_context': ''
        }
        res_report = session.post(urlrep, data=data_spam)
        if res_report.text.find("Your reports help keep our community free of spam.") >= 0:
            print(f"[+] Done Spam: {done_spam}")
            done_spam += 1
            sleep(sleep_time)
        else:
            print(f"[+]Error Spam: {done_spam}")
            error_spam += 1
            sleep(20)


if __name__ == '__main__':
    login()
