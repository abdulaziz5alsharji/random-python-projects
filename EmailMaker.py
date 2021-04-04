import sys

try:
    import os
    from pyfiglet import figlet_format
    from termcolor import colored
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input("Press Any Key To Exit ..")
    sys.exit()


def emailMaker(file_name: str, name="email.txt") -> None:
    try:
        data = open(file_name, mode="r").read().split()
        for line in data:
            with open(name, mode="a") as file:
                file.write(f"{line}@gmail.com" + "\n")
    except Exception as e:
        print(colored(e, color="red"))
        sys.exit()


if __name__ == '__main__':
    try:
        print()
        print(colored(figlet_format("Email Maker"), color="blue"))
        print("\n")
        FileName = input(colored("[?]File Name >>", color="green"))
        Name = input(colored("[?]Name >>", color="green"))
        emailMaker(file_name=FileName, name=Name)
        print("\n")
        print(colored(f"Done >> {Name}", color="blue"))
    except Exception as er:
        print(colored(er, color="red"))
        sys.exit()
