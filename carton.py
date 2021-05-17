import sys

try:
    import os
    from platform import system
    from pyfiglet import figlet_format
    from termcolor import colored
    from cowsay import *
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!]Press Any Key To Exit ..", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def showCarton(character, string: str) -> None:
    character(string)


if __name__ == '__main__':
    try:
        characters = {
            1: 'beavis',
            2: 'cheese',
            3: 'daemon',
            4: 'cow',
            5: 'dragon',
            6: 'ghostbusters',
            7: 'kitty',
            8: 'meow',
            9: 'milk',
            10: 'pig',
            11: 'stegosaurus',
            12: 'stimpy',
            13: 'trex',
            14: 'turkey',
            15: 'turtle',
            16: 'tux'}
        clear()
        print()
        print(colored(figlet_format("CARTON"), color="blue"))
        print("\n")
        for number, item in enumerate(char_names, start=1):
            print(colored(f"[{number}] {item}", color="blue"))
        print("\n")
        option = int(input(colored("[+]Choose Number: ", color="blue")))
        showCarton(eval(characters.get(option, colored("[!]INVALID NUMBER", color="red"))), "Hello world")
    except SyntaxError:
        print(colored("[!]INVALID NUMBER", color="red"))
