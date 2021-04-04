import sys

try:
    from pyfiglet import figlet_format
    import os
    from termcolor import colored
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input("Press Any Key To Exit ...")
    sys.exit()

clear = lambda: os.system("cls")


def combo(users_file: str, pass_file: str, combo_name="combo.txt") -> None:
    try:
        users = open(users_file, "r").read().split()
        passwords = open(pass_file, "r").read().split()
        for user in users:
            for password in passwords:
                with open(combo_name, "a") as combo_file:
                    combo_file.write(f"{user}:{password}" + "\n")
    except Exception as e:
        print(colored(e, color="red"))
        sys.exit()


if __name__ == '__main__':
    clear()
    try:
        print()
        print(colored(figlet_format("COMBO"), color="blue"))
        print("\n")
        first_file = input(colored("[?]First File >>", color="green"))
        second_file = input(colored("[?]Second File >>", color="green"))
        comboFile = input(colored("[?]Combo Name >>", color="green"))
        combo(
            users_file=first_file,
            pass_file=second_file,
            combo_name=comboFile
        )
        print("\n")
        print(colored("[+]Done", color="blue"))
    except Exception as er:
        print(colored(er, color="red"))
        sys.exit()
