import sys

try:
    import os
    from PIL import Image
    from pyfiglet import figlet_format
    from termcolor import colored
    from platform import system
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input("Press Any Key To Exit ...")
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def pngToIcon(image_path: str, icon_name="logo.ico") -> None:
    try:
        filename = image_path
        image = Image.open(filename)
        image.save(icon_name, format="ICO", sizes=[(32, 32)])
    except Exception as e:
        print(colored(e, color="red"))
        sys.exit()


if __name__ == '__main__':
    try:
        clear()
        print()
        print(colored(figlet_format("PNG TO ICON"), color="blue"))
        print("\n")
        ImagePath = input(colored("[?]Image Path >>", color="blue"))
        IconName = input(colored("[?]Icon Name >>", color="blue"))
        pngToIcon(
            image_path=ImagePath,
            icon_name=f"{IconName}.ico"
        )
        print()
        print(colored("[+]Done", color="blue"))
    except Exception as er:
        print(colored(er, color="red"))
        sys.exit()
