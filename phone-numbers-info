import sys

try:
    from phonenumbers import parse
    from phonenumbers import geocoder
    from phonenumbers import carrier
    from termcolor import colored
    from pyfiglet import figlet_format
except ModuleNotFoundError as error:
    print(error)
    input("Press Any Key To Exit ..")
    sys.exit()


# Start Class
class PhoneNumberInfo:
    def __init__(self, phone_number: str) -> None:
        self.phone_number = phone_number

    def find_country(self, lang="en") -> str:
        try:
            number = parse(self.phone_number, "CH")

            return geocoder.description_for_number(number, lang)
        except Exception as e:
            print(colored(e, color="red"))
            sys.exit()

    def find_network_company(self, lang="en") -> str:
        try:
            number = parse(self.phone_number, "RO")

            return carrier.name_for_number(number, lang)
        except Exception as e:
            print(colored(e, color="red"))
            sys.exit()

    @staticmethod
    def about() -> None:
        print("Coding By instagram >> @5ab_f")


if __name__ == '__main__':
    print(colored("\t-------------------------welcome----------------------------", color="blue"))
    print(colored(figlet_format("PHONE NUMBER"), color="blue"))
    print("\n")
    print(colored("""
[+]Find Country => (1)
[+]Find Network Company => (2)
[+]Exit => (99)
    """, color="blue"))
    print()
    mode = int(input(colored("[?] Choose Mode >>", color="green")))
    if mode == 1:
        phone = input(colored("[?]Phone Number >>", color="green"))
        info = PhoneNumberInfo(phone_number=phone)
        print()
        print(colored(f"[!]The Country Is: {info.find_country()}", color="green"))
    elif mode == 2:
        phone = input(colored("[?]Phone Number >>", color="green"))
        info = PhoneNumberInfo(phone_number=phone)
        print()
        print(colored(f"[!]The Network Company Is: {info.find_network_company()}", color="green"))
    elif mode == 99:
        print(colored("Good Bye", color="green"))
        sys.exit()
    else:
        print(colored("Wrong Choices", color="red"))
