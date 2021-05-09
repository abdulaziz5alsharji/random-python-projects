import sys

try:
    import os
    from platform import system
    from mailer import Mailer
    from pyfiglet import figlet_format
    from termcolor import colored
except ModuleNotFoundError as e:
    print(colored(e, color="red"))
    input(colored("[!]Press Any Key To Exit ..", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


class SendEmailMessage:
    def __init__(self, email: str, password: str, dear: str, subject: str, msg: str) -> None:
        self.yourEmail = email
        self.password = password
        self.dear = dear
        self.subject = subject
        self.message = msg

    def sendMessage(self) -> str:
        try:
            mail = Mailer(self.yourEmail, self.password)

            mail.send(receiver=self.dear,  # Email From Any service Provider
                      subject=self.subject,
                      message=self.message)
            if mail.status:
                return "Done send!.."
            else:
                return "Error"
        except Exception as error:
            print(colored(error, color="red"))
            sys.exit()


if __name__ == '__main__':
    clear()
    print()
    print(colored(figlet_format("E-MAIL MESSAGE"), color="blue"))
    print("\n")
    EMAIL = input(colored("E-Mail :", color="blue"))
    PASSWORD = input(colored("Password :", color="blue"))
    DEAR = input(colored("To :", color="blue"))
    SUB = input(colored("Subject :", color="blue"))
    MSG = input(colored("Message :", color="blue"))
    print("\n")
    sender = SendEmailMessage(email=EMAIL, password=PASSWORD, dear=DEAR, subject=SUB, msg=MSG)
    print(colored(f"[+]{sender.sendMessage()}", color="blue"))
