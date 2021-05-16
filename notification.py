import sys

try:
    import os
    from platform import system
    from pyfiglet import figlet_format
    from termcolor import colored
    from pynotifier import Notification
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!]Press Any Key To Exit ..", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def notification(title: str, description: str, icon_path=None, duration=5) -> None:
    try:
        Notification(title=title, description=description, icon_path=icon_path, duration=duration).send()
    except Exception as e:
        print(colored(e, color="red"))
        sys.exit()


if __name__ == '__main__':
    try:
        clear()
        print()
        print(colored(figlet_format("Notification"), color="blue"))
        print("\n")
        Title = input(colored("[?]Title: ", color="blue"))
        Description = input(colored("[?]Description: ", color="blue"))
        iconPath = input(colored("[?]Icon Path: ", color="blue"))
        Duration = int(input(colored("[?]Duration: ", color="blue")))
        notification(
            title=Title,
            description=Description,
            icon_path=iconPath,
            duration=Duration
        )
    except ValueError as er:
        print(colored(er, color="red"))
        sys.exit()

