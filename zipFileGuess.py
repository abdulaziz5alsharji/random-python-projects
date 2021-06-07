import sys

try:
    import os
    import zipfile
    from platform import system
    from termcolor import colored
    from pyfiglet import figlet_format
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[+]Press Any Key To Exit .. ", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def guessZipFile(zip_file: str, password_file: str, output: str) -> None:
    zipFile = zipfile.ZipFile(zip_file, "r")
    with open(password_file, "r") as file:
        passwords = file.read().split()
        for password in passwords:
            try:
                zipFile.extractall(output, pwd=password.encode("UTF-8"))
                print(colored(f"[+]Password Found: {password}", color="blue"))
                break
            except RuntimeError:
                print(colored(f"[+]Invalid Password: {password}", color="red"))


if __name__ == '__main__':
    try:
        clear()
        print()
        print(colored(figlet_format("Zip File Guess"), color="blue"))
        print("\n")
        ZIPFILE = input(colored("[+]Zip File (example.zip): ", color="blue"))
        PASS = input(colored("[+]Password File (example.txt): ", color="blue"))
        OUTPUT = input(colored("[+]Output Path (Any Path): ", color="blue"))
        print("\n")
        guessZipFile(
            zip_file=ZIPFILE,
            password_file=PASS,
            output=OUTPUT
        )
    except Exception as err:
        print(colored(err, color="red"))

