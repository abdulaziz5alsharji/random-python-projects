import sys

try:
    import os
    from termcolor import colored
    from pyfiglet import figlet_format
    from platform import system
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!]Press Any Key To Exit...", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


class SendEmail:
    """
    Send Message using python (smtp).
    """

    def __init__(self, email: str, password: str, email_target: str, subject: str, msg: str) -> None:
        self.email = email
        self.password = password
        self.emailTarget = email_target
        self.subject = subject
        self.message = msg

    def sendMessage(self) -> None:
        try:
            message = MIMEMultipart()
            message["From"] = self.email
            message["To"] = self.emailTarget
            message["Subject"] = self.subject
            message.attach(MIMEText(self.message, "plain"))
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(self.email, self.password)
            msg = message.as_string()
            server.sendmail(self.email, self.emailTarget, msg)
            server.quit()
        except Exception as er:
            print(colored(er, color="red"))
            sys.exit()


def sendOneMessage(email: str, password: str, target: str, subject: str, msg: str) -> None:
    emailSender = SendEmail(
        email=email,
        password=password,
        email_target=target,
        subject=subject,
        msg=msg
    )
    emailSender.sendMessage()
    print(colored("[+]Send Is Done -_-", color="blue"))


def sendMessages(email: str, password: str, target: str, subject: str, msg: str, num_of_msg: int) -> None:
    for counter in range(1, num_of_msg + 1):
        emailSender = SendEmail(
            email=email,
            password=password,
            email_target=target,
            subject=subject,
            msg=msg
        )
        emailSender.sendMessage()
        print(colored(f"\r[+]SENT: {counter}", color="blue"), end="")


def sendMessagesToRandomTarget(email: str, password: str, file_emails: str, subject: str, msg: str) -> None:
    try:
        emails = open(file_emails, "r").read().split()
        for target in emails:
            emailSender = SendEmail(
                email=email,
                password=password,
                email_target=target,
                subject=subject,
                msg=msg
            )
            emailSender.sendMessage()
            print(colored(f"[+]SEND TO: {target} IS DONE.", color="blue"))
    except Exception as err:
        print(colored(err, color="red"))
        sys.exit()


if __name__ == '__main__':
    clear()
    print()
    print(colored(figlet_format("Email Sender Tool"), color="blue"))
    print("\n")
    print(colored("""
[1]Send One Message
[2]Send Many Message
[3]Send Message To Random Targets
[99]Exit
""", color="blue"))
    print("\n")
    try:
        option = int(input(colored("[+]OPTION >(1, 2, 3, 99): ", color="blue")))
        print("\n")
        if option == 1:
            EMAIL = input(colored("[+]Email: ", color="blue"))
            PASS = input(colored("[+]Password: ", color="blue"))
            EMAIL_TO = input(colored("[+]Email Target: ", color="blue"))
            SUBJECT = input(colored("[+]Subject: ", color="blue"))
            MESSAGE = input(colored("[+]Message: ", color="blue"))
            print("\n")
            sendOneMessage(
                email=EMAIL,
                password=PASS,
                target=EMAIL,
                subject=SUBJECT,
                msg=MESSAGE
            )
        elif option == 2:
            EMAIL = input(colored("[+]Email: ", color="blue"))
            PASS = input(colored("[+]Password: ", color="blue"))
            EMAIL_TO = input(colored("[+]Email Target: ", color="blue"))
            SUBJECT = input(colored("[+]Subject: ", color="blue"))
            MESSAGE = input(colored("[+]Message: ", color="blue"))
            NumberOfMessage = int(input(colored("[+]Messages Number: ", color="blue")))
            print("\n")
            sendMessages(
                email=EMAIL,
                password=PASS,
                target=EMAIL,
                subject=SUBJECT,
                msg=MESSAGE,
                num_of_msg=NumberOfMessage
            )
        elif option == 3:
            EMAIL = input(colored("[+]Email: ", color="blue"))
            PASS = input(colored("[+]Password: ", color="blue"))
            emailFile = input(colored("[+]Email File: ", color="blue"))
            SUBJECT = input(colored("[+]Subject: ", color="blue"))
            MESSAGE = input(colored("[+]Message: ", color="blue"))
            print("\n")
            sendMessagesToRandomTarget(
                email=EMAIL,
                password=PASS,
                file_emails=emailFile,
                subject=SUBJECT,
                msg=MESSAGE,
            )
        elif option == 99:
            sys.exit()
        else:
            print(colored("[!]INVALID OPTION", color="red"))
    except ValueError:
        print("\n")
        print(colored("[!]INVALID OPTION", color="red"))
        sys.exit()
