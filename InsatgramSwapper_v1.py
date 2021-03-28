try:
    import requests, secrets
    import uuid
    import threading
    from tkinter import messagebox
    from pyfiglet import figlet_format
except ModuleNotFoundError as e:
    import sys

    print(e)
    input("Enter to exit...")
    sys.exit()


class Swapper:
    def __init__(self, username: str, password: str, target: str, thread_number: int) -> None:
        self.username = username
        self.password = password
        self.target = target
        self.thread_number = thread_number
        self.cookie = secrets.token_hex(8) * 2
        self.uid = uuid.uuid4()
        self.done = 1
        self.session = requests.Session()
        self.login()

    # Login Method
    def login(self):
        self.login_url = "https://www.instagram.com/accounts/login/ajax/"
        self.login_data = {
            "username": self.username,
            "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:1609186862:{self.password}",
            "queryParams": "{}",
            "optIntoOneTap": "false"
        }
        self.header = {
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
            "mid": self.cookie
        }
        self.res_login = self.session.post(self.login_url, headers=self.header, data=self.login_data,
                                           allow_redirects=True)
        self.cookies = self.res_login.cookies
        if self.res_login.json()["authenticated"] == True:
            print(f"[√] LOGIN DONE :{self.username}")
            self.session.headers.update({'X-CSRFToken': self.res_login.cookies['csrftoken']})
            self.info()
        else:
            print(f"[x] ERROR LOGIN :{self.username}")

    # Info Method
    def info(self):
        self.info_url = "https://www.instagram.com/accounts/edit/?__a=1"
        self.res_info = self.session.get(self.info_url).json()
        self.first_name = self.res_info["form_data"]["first_name"]
        self.phone_number = self.res_info["form_data"]["phone_number"]
        self.email = self.res_info["form_data"]["email"]
        self.thread()

    # swap Method
    def swap(self):
        while True:
            self.swap_url = "https://www.instagram.com/accounts/edit/"
            self.swap_data = {
                "first_name": self.first_name,
                "email": self.email,
                "username": self.target,
                "phone_number": self.phone_number,
                "biography": "swapper by @5ab_f",
                "external_url": "",
                "chaining_enabled": "on"
            }
            self.res_swap = self.session.post(self.swap_url, data=self.swap_data)
            if self.res_swap.status_code == 200:
                print(f"DONE >>@{self.target}")
                messagebox.showinfo("Swapper by @5ab_f", f"done >>@{self.target}")
                break
            elif self.res_swap.status_code == 429:
                print(f"Blocked >>@{self.target}=>{self.done}")
                self.done += 1
            else:
                print(f"Trying {self.done}")
                self.done += 1

    # threading Method
    def thread(self):
        self.threads = []
        for i in range(self.thread_number):
            self.t = threading.Thread(target=self.swap)
            self.t.start()
            self.threads.append(self.t)
        for thread in self.threads:
            thread.join()


if __name__ == "__main__":
    print(figlet_format("SWAPPER"))
    username = input("USER >>")
    password = input("PASSWORD >>")
    target = input("TARGET >>")
    thread_number = int(input("Threading >>"))
    Swapper(username=username, password=password, target=target, thread_number=thread_number)
