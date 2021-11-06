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
    input(colored("[!!]Press Any Key To Exit..", "red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def password_generator(length: int) -> str:
    all_char = string.ascii_letters + string.digits + string.punctuation
    password = "".join([random.choice(all_char) for _ in range(length)])
    return password


if __name__ == '__main__':
    clear()
    print(colored(figlet_format("Password Generator"), color="blue"))
    print("")
    try:
        LENGTH = int(input(colored("[+]Password Length: ", color="blue")))
        print("\n")
        print(colored(f"Password: {password_generator(LENGTH)}", color="blue"))
    except ValueError as er:
        print(colored(er, color="red"))
        input(colored("[!!]Press Any Key To Exit..", "red"))
        sys.exit()

