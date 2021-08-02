import sys

try:
    import os
    from hashlib import (md5, sha1, sha256, sha384, sha512, sha224)
    from pyfiglet import figlet_format
    from termcolor import colored
    from platform import system
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!]Press Any Key To Exit .. ", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def decodeHash(hash_type, hashing: str) -> str:
    try:
        with open("randomWords.txt", "r") as file:
            arrWords = file.read().split()
            for word in arrWords:
                if hash_type(word.encode()).hexdigest() == hashing:
                    return colored(f"[+]Unscrewed:{word}", color="blue")
    
        return colored("[+]Not Found", color="red")
    except Exception as err:
        print(colored(err, color="red"))
        input(colored("[!]Press Any Key To Exit .. ", color="red"))
        sys.exit()


if __name__ == '__main__':
    HASH_TYPE = {
        1: md5,
        2: sha1,
        3: sha256,
        4: sha384,
        5: sha512,
        6: sha224,
    }
    clear()
    print()
    print(colored(figlet_format("Hash Decode"), color="blue"))
    print("\n")
    print(colored("""
[1]md5
[2]sha1
[3]sha256
[4]sha384
[5]sha512
[6]sha224
[0]Exit
""", color="blue"))
    print("\n")
    try:
        option = int(input(colored("[++]Option: ", color="blue")))
        print("\n")
        if option == 0:
            input(colored("[!]Press Any Key To Exit .. ", color="blue"))
            sys.exit()
        elif option in [1, 2, 3, 4, 5, 6]:
            HASHING = input(colored("[+]Hash : ", color="blue"))
            print("\n")
            print(decodeHash(HASH_TYPE[option], HASHING))
        else:
            print(colored("[!!]Invalid Option", color="red"))
            input(colored("[!]Press Any Key To Exit .. ", color="red"))
            sys.exit()
    except ValueError as er:
        print(colored("[!!]Invalid Option", color="red"))
        input(colored("[!]Press Any Key To Exit .. ", color="red"))
