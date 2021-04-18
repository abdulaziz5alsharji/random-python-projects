import sys

try:
    import os
    from platform import system
    from pyfiglet import figlet_format
    from termcolor import colored
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input("[+]Press Any Key To Exit ..")
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def getIpWebsite(url: str) -> None:
    os.system(f"ping {url}")


def getYourIpAddress() -> None:
    os.system("ipconfig")


# IPv4 Address

if __name__ == '__main__':
    try:
        clear()
        print()
        print(colored(figlet_format("GET IP"), color="blue"))
        print("\n")
        print(colored("""
[-]Get Your IPv4 Address [1]
[-]Get Website IP Address [2]
[-]Exit [99]
        """, color="blue"))
        mode = int(input(colored("[?] Your Choose >>", color="blue")))
        if mode == 1:
            getYourIpAddress()
        elif mode == 2:
            URL = input(colored("[?] Website Url >>", color="blue"))
            getIpWebsite(url=URL)
        elif mode == 99:
            sys.exit()
        else:
            print(colored("[</>] Choose 1 or 2 or 99", color="red"))
            sys.exit()
    except Exception as er:
        print(colored(er, color="red"))
        sys.exit()
