import sys

try:
    import os
    import calendar
    from platform import system
    from pyfiglet import figlet_format
    from termcolor import colored
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!]Press Any Key To Exit ..", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def showCalender(year: int, month: int) -> str:
    return calendar.month(year, month)


if __name__ == '__main__':
    try:
        clear()
        print()
        print(colored(figlet_format("Calender"), color="blue"))
        print("\n")
        YEAR = int(input(colored("[+]Year: ", color="blue")))
        MONTH = int(input(colored("[+]Month: ", color="blue")))
        print("\n")
        print(colored(showCalender(year=YEAR, month=MONTH), color="blue"))
    except ValueError as er:
        print(colored(er, color="red"))
        sys.exit()
