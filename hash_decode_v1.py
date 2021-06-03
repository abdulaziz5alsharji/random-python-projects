import sys

try:
    import os
    from hashlib import md5
    from pyfiglet import figlet_format
    from termcolor import colored
    from platform import system
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!]Press Any Key To Exit .. ", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def decodeMD5(hashing: str) -> str:
    with open("randomWords.txt", "r") as file:
        arrWords = file.read().split()
        for word in arrWords:
            if md5(word.encode()).hexdigest() == hashing:
                return colored(f"[+]Unscrewed:{word}", color="blue")

    return colored("[+]Not Found", color="red")


if __name__ == '__main__':
    clear()
    print()
    print(colored(figlet_format("MD5 Decode"), color="blue"))
    print("\n")
    HASHING = input(colored("[+]Hash [md5 only]: ", color="blue"))
    print("\n")
    print(decodeMD5(hashing=HASHING))
