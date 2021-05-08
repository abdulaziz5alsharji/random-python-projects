import sys

try:
    import os
    import requests
    import uuid
    from platform import system
    from pyfiglet import figlet_format
    from termcolor import colored
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!]Press Any Key To Exit...", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


class InstagramMessageSender:
    def __init__(self, username: str, password: str, target: str, msg: str, msg_num: int) -> None:
        self.username = username
        self.password = password
        self.target = target
        self.msg = msg
        self.msg_num = msg_num
        self.session = requests.session()
        self.uuid = uuid.uuid4()
        self.headers = {
            'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; '
                          'angler; angler; en_US)',
            'Accept': "/",
            'Cookie': 'missing',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-Connection-Type': 'WIFI',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'i.instagram.com'

        }

    def login(self):
        urlLogin = "https://i.instagram.com/api/v1/accounts/login/"
        dataLogin = {
            'uuid': self.uuid,
            'password': self.password,
            'username': self.username,
            'device_id': self.uuid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'
        }
        headersLogin = {
            'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; '
                          'angler; angler; en_US)',
            'Accept': "/",
            'Cookie': 'missing',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-Connection-Type': 'WIFI',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'i.instagram.com'

        }
        try:
            loginRequest = self.session.post(url=urlLogin, data=dataLogin, headers=headersLogin, allow_redirects=True)
            jsonData = loginRequest.json()
            if not jsonData["logged_in_user"]["is_private"]:
                print(colored(f"\t[√]Login Done: {self.username}", color="blue"))
                self.headers.update({'Cookie': f'csrftoken={loginRequest.cookies["csrftoken"]}; sessionid={loginRequest.cookies["sessionid"]}; mid={loginRequest.cookies["mid"]}'})
        except KeyError:
            print(colored(f"\t[x]Login Error: {self.username}", color="red"))
            sys.exit()

    def getUserId(self):
        userIdUrl = f"https://i.instagram.com/api/v1/users/{self.target}/usernameinfo/"
        userIdRequest = self.session.get(url=userIdUrl, headers=self.headers).json()
        try:
            userId = userIdRequest["user"]["pk"]
            return userId
        except KeyError:
            return colored(f"[!]TARGET: {self.target} > NOT FOUND", color="red")

    def sendMessage(self):
        messageId = 679397915473
        counter = 1
        errors = 1
        for _ in range(self.msg_num):
            sendUrl = "https://i.instagram.com/api/v1/direct_v2/threads/broadcast/text/"
            sendData = {
                'recipient_users': f'[[{self.getUserId()}]]',
                'action': 'send_item',
                'is_shh_mode': 0,
                'send_attribution': 'inbox_search',
                'client_context': f'{messageId}',
                'text': f'{self.msg}',
                'device_id': f'{uuid.uuid4()}',
                'mutation_token': f'{messageId}',
                '_uuid': f'{uuid.uuid4()}',
                'offline_threading_id': f'{messageId}'
            }
            rendRequest = self.session.post(url=sendUrl, data=sendData, headers=self.headers).json()
            if rendRequest["status"] == "ok":
                print(colored(f"\r\t[{counter}] Done Send Message To : @{self.target}", color="blue"), end="")
                counter += 1
            else:
                print(colored(f"\r\t[{errors}] Error Send Message To : @{self.target}", color="blue"), end="")
                errors += 1
            messageId += 5

    def run(self):
        self.login()
        self.sendMessage()


if __name__ == '__main__':
    clear()
    print()
    print(colored(figlet_format("Message Sender"), color="blue"))
    print("\n")
    USERNAME = input(colored("[+]USERNAME: ", color="blue"))
    PASSWORD = input(colored("[+]PASSWORD: ", color="blue"))
    TARGET = input(colored("[+]TARGET: ", color="blue"))
    MSG = input(colored("[+]MESSAGE: ", color="blue"))
    numberOfMsg = int(input(colored("[+]NUMBER OF MESSAGE: ", color="blue")))
    sender = InstagramMessageSender(USERNAME, PASSWORD, TARGET, MSG, numberOfMsg)
    sender.run()
