import sys

try:
    import os
    from platform import system
    from termcolor import colored
    from pyfiglet import figlet_format
    import pyshorteners
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input("[+]Press Any Key To Exit ..")
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def shorter_url(url: str) -> str:
    try:
        shorter = pyshorteners.Shortener()
        return shorter.tinyurl.short(url)
    except Exception as er:
        print(colored(er, color="red"))
        sys.exit()


if __name__ == '__main__':
    try:
        clear()
        print()
        print(colored(figlet_format("URL-SHORTER"), color="blue"))
        print("\n")
        URL = input(colored("[?]ENTER URL :", color="blue"))
        print()
        print(colored(f"[+]LINK: {shorter_url(URL)}", color="blue"))
    except Exception as e:
        print(colored(e, color="red"))
        sys.exit()

