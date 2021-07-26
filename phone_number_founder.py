import sys

try:
    import os
    import requests
    from platform import system
    from termcolor import colored
    from pyfiglet import figlet_format
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!!]Press Any Key To Exit..", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def find(phone_number: int, country: str) -> str:
    url = f"http://caller-id.saedhamdan.com/index.php/UserManagement/search_number?number={phone_number}&country_code={country}"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/87.0.4280.88 Safari/537.36"
    }
    response = requests.get(url, headers=headers).json()
    if response["msg"] == "Record found.":
        return response["result"][0]["name"]

    return "[!!]NOT FOUND !!"


if __name__ == '__main__':
    clear()
    print()
    print(colored(figlet_format("PHONE number founder"), color="blue"))
    print("\n")
    print(colored("""
[1]OMN
[2]KWT
[3]KSA
[4]UAE
[5]QTR
[6]BHR
[0]Exit
""", color="blue"))
    print("\n")
    try:
        option = int(input(colored("Option: ", color="blue")))
        print("\n")
        if option == 1:
            phoneNumber = int(input(colored("Phone Number: ", color="blue")))
            print("")
            print(colored(f"Name: {find(phoneNumber, country='OM')}", color="blue"))
        elif option == 2:
            phoneNumber = int(input(colored("Phone Number: ", color="blue")))
            print("")
            print(colored(f"Name: {find(phoneNumber, country='KW')}", color="blue"))
        elif option == 3:
            phoneNumber = int(input(colored("Phone Number: ", color="blue")))
            print("")
            print(colored(f"Name: {find(phoneNumber, country='SA')}", color="blue"))
        elif option == 4:
            phoneNumber = int(input(colored("Phone Number: ", color="blue")))
            print("")
            print(colored(f"Name: {find(phoneNumber, country='AE')}", color="blue"))
        elif option == 5:
            phoneNumber = int(input(colored("Phone Number: ", color="blue")))
            print("")
            print(colored(f"Name: {find(phoneNumber, country='QA')}", color="blue"))
        elif option == 6:
            phoneNumber = int(input(colored("Phone Number: ", color="blue")))
            print("")
            print(colored(f"Name: {find(phoneNumber, country='BH')}", color="blue"))
        elif option == 0:
            sys.exit()
        else:
            print(colored("[!!]Invalid Option...", color="red"))
    except ValueError as er:
        print(colored(er, color="red"))
        input(colored("[!!]Press Any Key To Exit..", color="red"))
        sys.exit()


