import sys

try:
    import os
    from platform import system
    from pyfiglet import figlet_format
    from termcolor import colored
    from forex_python.converter import CurrencyRates
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!]Press Any Key To Exit ..", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def getRate(first_currency: str, second_currency: str) -> float:
    currency = CurrencyRates()
    return currency.get_rate(first_currency, second_currency)


def Convert(currency_one: str, currency_two: str, price: float) -> float:
    currency = CurrencyRates()
    return currency.convert(currency_one, currency_two, price)


def main():
    try:
        clear()
        print()
        print(colored(figlet_format("Convert Currency"), color="blue"))
        print("\n")
        print(colored("""
[1]Get Rate
[2]Convert Currency
[99]Exit   
    """, color="blue"))
        print()
        yourChoices = int(input(colored("[?]Choose:", color="blue")))
        print("\n")
        if yourChoices == 1:
            firstCurrency = input(colored("[?]First Currency:", color="blue"))
            secondCurrency = input(colored("[?]Second Currency:", color="blue"))
            print(colored(f"The Rate is: {getRate(firstCurrency, secondCurrency)}", color="blue"))
        elif yourChoices == 2:
            firstCurrency = input(colored("[?]First Currency:", color="blue"))
            secondCurrency = input(colored("[?]Second Currency:", color="blue"))
            PRICE = float(input(colored("[?]Price:", color="blue")))
            print(colored(f"The Rate is: {Convert(firstCurrency, secondCurrency, PRICE)}", color="blue"))
        elif yourChoices == 99:
            print(colored("[-]GoodBye", color="blue"))
            sys.exit()
        else:
            print(colored("[!]ERROR CHOiCES", color="red"))
            sys.exit()
    except Exception as e:
        print(colored(e, color="red"))
        sys.exit()


if __name__ == '__main__':
    main()
