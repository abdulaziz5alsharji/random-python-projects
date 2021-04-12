import sys

try:
    import os
    from platform import system
    from termcolor import colored
    from pyfiglet import figlet_format
    from pyzbar.pyzbar import decode
    from PIL import Image
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input("[!]Press Any Key To Exit ..")
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def decodeData(image_name: str) -> str:
    try:
        image = Image.open(image_name)
        data = decode(image)
        return data[0].data.decode()
    except Exception as e:
        print(colored(e, color="red"))
        sys.exit()


if __name__ == '__main__':
    clear()
    print()
    print(colored(figlet_format("Decode DATA"), color="blue"))
    print("\n")
    ImageName = input(colored("[?]Image Name >>", color="blue"))
    DATA = decodeData(
        image_name=ImageName
    )
    print(colored(f"[+]THE DATA IS {DATA}", color="blue"))
