import sys

try:
    import os
    import random
    import string
    from platform import system
    from termcolor import colored
    from pyfiglet import figlet_format
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!]Press Any Key To Exit ..", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def randomPassword(length: int) -> str:
    letterAndDigits = [*string.digits, *string.ascii_letters]
    return "".join(random.choice(letterAndDigits) for _ in range(length))


if __name__ == '__main__':
    clear()
    print()
    print(colored(figlet_format("Password Generator"), color="blue"))
    print("\n")
    try:
        lengthOfPassword = int(input(colored("[+]Password Length: ", color="blue")))
        numberOfPassword = int(input(colored("[+]Password Number: ", color="blue")))
        fileName = str(input(colored("[+]File Name: ", color="blue")))
        file = open(fileName, "a")
        for _ in range(numberOfPassword):
            password = randomPassword(lengthOfPassword)
            file.write(password+"\n")
            print(colored(f"[+]{password}", color="blue"))
        print("")
        print(colored(f"[+]Done: {fileName}", color="blue"))
    except ValueError as er:
        print(colored(er, color="red"))
        sys.exit()
