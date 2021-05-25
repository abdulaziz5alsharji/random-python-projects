import sys

try:
    import os
    import pytesseract
    from PIL import Image
    from platform import system
    from pyfiglet import figlet_format
    from termcolor import colored
except Exception as error:
    print(colored(error, color="red"))
    input(colored("[+]Press Any Key To Exit ..", color="red"))
    sys.exit()

# To Clean The Terminal
clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def imageToText(image_name: str) -> str:
    image = Image.open(image_name)
    return pytesseract.image_to_string(image)


if __name__ == '__main__':
    clear()
    print()
    print(colored(figlet_format("IMAGE TO TEXT"), color="blue"))
    print("\n")
    try:
        imageName = input(colored("[+]Image Name: ", color="blue"))
        print("\n")
        print(imageToText(image_name=imageName))
    except Exception as er:
        print(colored(er, color="red"))
