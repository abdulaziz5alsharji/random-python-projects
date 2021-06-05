import sys

try:
    import os
    import requests
    from platform import system
    from pyfiglet import figlet_format
    from termcolor import colored
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!]Press Any Key To Exit .. ", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def adminFounder(url: str) -> None:
    with open("admin_paths.txt", "r") as file:
        paths = file.read().split()
        for path in paths:
            fullUrl = f"{url}/{path}"
            response = requests.get(url=fullUrl).status_code
            if response == 200:
                print("\n")
                print(colored(f"[+]Found: {fullUrl}", color="green"))
                break
            else:
                print(colored(f"\r[+]Not Found: {fullUrl}", color="red"), end="")


if __name__ == '__main__':
    clear()
    print()
    print(colored(figlet_format("Admin Founder"), color="blue"))
    print("\n")
    URL = input(colored("[+]Url: ", color="blue"))
    print("\n")
    adminFounder(url=URL)