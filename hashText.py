import sys

try:
    from hashlib import (md5, sha1, sha256, sha512, sha384, sha224)
    import os
    from platform import system
    from pyfiglet import figlet_format
    from termcolor import colored
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!]Press Any Key To Exit .."))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


class HashText:
    def __init__(self, string: str) -> None:
        self.string = string.encode()

    def Md5(self) -> str:
        return md5(self.string).hexdigest()

    def Sha1(self) -> str:
        return sha1(self.string).hexdigest()

    def Sha256(self) -> str:
        return sha256(self.string).hexdigest()

    def Sha512(self) -> str:
        return sha512(self.string).hexdigest()

    def Sha224(self) -> str:
        return sha224(self.string).hexdigest()


def main():
    clear()
    print()
    print(colored(figlet_format("HASHING"), color="blue"))
    print("\n")
    print(colored("""
[1]MD5
[2]SHA1 
[3]SHA224 
[4]SHA512 
[5]SHA256
[99]EXIT  
""", color="blue"))
    print("")
    try:
        option = int(input(colored("[-]OPTION: ", color="blue")))
        STRING = input(colored("[-]TEXT: ", color="blue"))
        HASH = HashText(string=STRING)
        print("")
        if option == 1:
            print(colored(f"THE HASH IS : {HASH.Md5()}", color="blue"))
        elif option == 2:
            print(colored(f"THE HASH IS: {HASH.Sha1()}", color="blue"))
        elif option == 3:
            print(colored(f"THE HASH IS: {HASH.Sha224()}", color="blue"))
        elif option == 4:
            print(colored(f"THE HASH IS: {HASH.Sha512()}", color="blue"))
        elif option == 5:
            print(colored(f"THE HASH IS: {HASH.Sha256()}", color="blue"))
        elif option == 99:
            sys.exit()
    except ValueError as er:
        print(colored(er, color="red"))


if __name__ == '__main__':
    main()
