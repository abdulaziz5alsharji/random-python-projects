import sys

try:
    import random
    import string
    import os
    import pyautogui
    from pyfiglet import figlet_format
    from termcolor import colored
    from platform import system
    from time import sleep
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!]Press Any Key To Exit .. ", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


class Sender:
    def __init__(self, num_msg: int, slp: float) -> None:
        self.numberMessage = num_msg
        self.wait = slp

    def sendMessage(self, message: str) -> None:
        for _ in range(self.numberMessage):
            pyautogui.typewrite(message)
            sleep(self.wait)
            pyautogui.press("enter")
            sleep(self.wait)

    def sendFromFile(self, file_name: str) -> None:
        counter = 0
        with open(file_name, "r") as file:
            messagesList = file.read().split()
            for message in messagesList:
                if counter == self.numberMessage:
                    break
                pyautogui.typewrite(message)
                sleep(self.wait)
                pyautogui.press("enter")
                sleep(self.wait)
                counter += 1

    def sendRandomMessages(self, msg_length: int) -> None:
        letters = [*string.ascii_letters]
        for _ in range(self.numberMessage):
            message = "".join([random.choice(letters) for _ in range(msg_length)])
            pyautogui.typewrite(message)
            sleep(self.wait)
            pyautogui.press("enter")
            sleep(self.wait)


if __name__ == '__main__':
    clear()
    print()
    print(colored(figlet_format("Sender"), color="blue"))
    print("\n")
    print(colored("""
[1]Send Messages
[2]Send Messages From File
[3]Send Random Messages
[99]Exit
    """, color="blue"))
    print("\n")
    try:
        option = int(input(colored("[+]Option: ", color="blue")))
        print("\n")
        if option == 1:
            Message = input(colored("[+]Message: ", color="blue"))
            MessageNumber = int(input(colored("[+]Message Number: ", color="blue")))
            SLP = float(input(colored("[+]Sleep: ", color="blue")))
            sender = Sender(
                num_msg=MessageNumber,
                slp=SLP
            )
            sender.sendMessage(message=Message)
        elif option == 2:
            FileName = input(colored("[+]File Name (example.txt): ", color="blue"))
            MessageNumber = int(input(colored("[+]Message Number: ", color="blue")))
            SLP = float(input(colored("[+]Sleep: ", color="blue")))
            sender = Sender(
                num_msg=MessageNumber,
                slp=SLP
            )
            sender.sendFromFile(file_name=FileName)
        elif option == 3:
            messageLength = int(input(colored("[+]Message Length: ", color="blue")))
            MessageNumber = int(input(colored("[+]Message Number: ", color="blue")))
            SLP = float(input(colored("[+]Sleep: ", color="blue")))
            sender = Sender(
                num_msg=MessageNumber,
                slp=SLP
            )
            sender.sendRandomMessages(msg_length=messageLength)
        elif option == 99:
            sys.exit()
        else:
            print(colored("[!]Invalid Option, [1, 2, 3, 99]", color="red"))
    except ValueError as er:
        print(colored(er, color="red"))
        sys.exit()
        
        
