try:
    import os
    from pyfiglet import figlet_format
    from termcolor import colored
except ModuleNotFoundError as error:
    import sys

    print(colored(error, color="red"))
    input("Press Any Key To Exit ..")
    sys.exit()


def show_wifi_password(wifi_name: str) -> None:
    os.system(f"netsh wlan show profile {wifi_name} key=clear")


clear = lambda: os.system("cls")


def main():
    print()
    print(colored(figlet_format("Wifi"), color="blue"))
    print()
    wifiName = input(colored("[?]Wifi Name >>", color="green"))
    print("\n")
    clear()
    os.system("color 3")
    show_wifi_password(wifi_name=wifiName)


if __name__ == '__main__':
    main()
