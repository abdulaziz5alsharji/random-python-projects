import sys

try:
    import os
    from platform import system
    from termcolor import colored
    from pyfiglet import figlet_format
    from pathlib import Path
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!!]Press Any Key To Exit...", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def searchAboutFile(file_name: str, folder=".") -> None:
    try:
        counter = 1
        for path in Path(folder).rglob(file_name):
            print(colored(f"[{counter}] {path.absolute()}", color="blue"))
            counter += 1
    except Exception as er:
        print(colored(er, color="red"))


if __name__ == '__main__':
    clear()
    print()
    print(colored(figlet_format("Search About File"), color="blue"))
    print("\n")
    fileName = input(colored("[++]File Name: ", color="blue"))
    Folder = input(colored("[++]Folder Path: ", color="blue"))
    print("\n")
    if Folder:
        searchAboutFile(fileName, folder=Folder)
    else:
        searchAboutFile(fileName)
