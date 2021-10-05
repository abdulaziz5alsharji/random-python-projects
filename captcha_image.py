import sys
from typing import Text

try:
    import os
    from termcolor import colored
    from pyfiglet import figlet_format
    from platform import system
    from captcha.image import ImageCaptcha
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!!]Press Any Key To Exit..", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def convert(text: Text, img_name: str) -> None:
    try:
        image = ImageCaptcha(width=300, height=300)
        image.write(text, img_name)
        print(colored("[+]DONE", color="blue"))
    except Exception as er:
        print(colored(er, color="blue"))
        sys.exit()


if __name__ == '__main__':
    clear()
    print(colored(figlet_format("Captcha Image"), color="blue"))
    print()
    TEXT = input(colored("[+]Text: ", color="blue"))
    IMAGE_NAME = input(colored("[+]Image Name: ", color="blue"))
    print("\n")
    convert(TEXT, IMAGE_NAME)
