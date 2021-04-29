# Don't forget to download this lib : pip install speedtest-cli
import sys

try:
    import os
    from platform import system
    from pyfiglet import figlet_format
    from termcolor import colored
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!]Press Any Key To Exit ...", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def internetTester() -> None:
    os.system("speedtest")


if __name__ == '__main__':
    clear()
    print(colored(figlet_format("SPEED TESTER"), color="blue"))
    os.system("color 3")
    internetTester()
