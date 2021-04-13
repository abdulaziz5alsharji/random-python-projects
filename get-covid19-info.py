import sys

try:
    import os
    from platform import system
    from covid import Covid
    from pyfiglet import figlet_format
    from termcolor import colored
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input("[+]Press Any Key To Exit ...")
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def get_covid_info(country: str) -> None:
    try:
        covid19 = Covid(source="worldometers")
        data = covid19.get_status_by_country_name(country)
        for key in data:
            print(colored(f"{key} ==> {data[key]}", color="blue"))
    except ValueError as er:
        print(colored(er, color="red"))
        sys.exit()


if __name__ == '__main__':
    try:
        clear()
        print()
        print(colored(figlet_format("COVID 19 INFO"), color="blue"))
        print("\n")
        COUNTRY = input(colored("[?]Type Country >>", color="blue"))
        print("\n")
        get_covid_info(country=COUNTRY)
    except Exception as e:
        print(colored(e, color="red"))

