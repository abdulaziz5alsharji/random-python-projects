import sys

try:
    from time import sleep
    import os
    import pyautogui
    from pyfiglet import figlet_format
    from termcolor import colored
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input("Press Any Key To Exit ..")
    sys.exit()

clear = lambda: os.system("cls")


def sender(msg: str, msg_num: int, slp=0.0) -> None:
    for _ in range(msg_num):
        pyautogui.typewrite(msg)
        sleep(slp)
        pyautogui.press("enter")
        sleep(slp)


if __name__ == '__main__':
    try:
        clear()
        print()
        print(colored(figlet_format("SENDER"), color="blue"))
        print("\n")
        Message = input(colored("[?]Type Message >>", color="green"))
        MessageNumber = int(input(colored("[?]Message Number >>", color="green")))
        SLP = float(input(colored("[?]Sleep >>", color="green")))
        sender(
            msg=Message,
            msg_num=MessageNumber,
            slp=SLP
        )
    except Exception as e:
        print("\n")
        print(colored(e, color="red"))
        sys.exit()


