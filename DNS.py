import sys

try:
    import dns.resolver
    import os
    from platform import system
    from pyfiglet import figlet_format
    from termcolor import colored
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!]Press Any Key To Exit ..", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def getDNSRecords(host: str, dns_record_type: str) -> None:
    try:
        result = dns.resolver.query(host, dns_record_type, raise_on_no_answer=False)
        for item in result:
            print(colored(item.to_text(), color="blue"))
    except Exception as err:
        print(colored(err, color="red"))
        sys.exit()


if __name__ == '__main__':
    try:
        clear()
        print()
        print(colored(figlet_format("DNS Records"), color="blue"))
        print("\n")
        Host = input(colored("[++]Host: ", color="blue"))
        recordsType = input(colored("[++]DNS Records Type: ", color="blue"))
        print("\n")
        getDNSRecords(Host, dns_record_type=recordsType)
    except Exception as er:
        print(colored(er, color="red"))
        sys.exit()
