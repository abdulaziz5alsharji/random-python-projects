import sys

try:
    import os
    import string
    import random
    from termcolor import colored
    from pyfiglet import figlet_format
    from platform import system
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!!]Press Any Key To Exit..", color="red"))
    sys.exit()


clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def makeSerial(length: int) -> str:
    allChars = [*string.ascii_letters + string.digits]
    serial = [random.choice(allChars) for _ in range(length)]
    return "".join(serial)


if __name__ == '__main__':
    try:
        clear()
        print()
        print(colored(figlet_format("Serial Maker"), color="blue"))
        print("\n")
        Length = int(input(colored("[++]Length: ", color="blue")))
        print("\n")
        print(colored(f"Serial: {makeSerial(length=Length)}", color="blue"))
    except ValueError as err:
        print(colored(err, color="red"))
        input(colored("[!!]Press Any Key To Exit..", color="red"))
        sys.exit()
