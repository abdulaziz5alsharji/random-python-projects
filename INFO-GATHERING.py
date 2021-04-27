import sys

try:
    import os
    import socket
    from platform import system
    from pyfiglet import figlet_format
    from termcolor import colored
    from urllib.request import urlopen
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!] Press Any Key To Exit ..", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


class InfoGathering:
    @staticmethod
    def machineName() -> str:
        return socket.gethostname()

    @staticmethod
    def localIp() -> str:
        return socket.gethostbyname(socket.gethostname())

    @staticmethod
    def websiteIp(domain) -> str:
        try:
            return socket.gethostbyname(domain)
        except Exception as e:
            print(colored(e, color="red"))
            sys.exit()

    @staticmethod
    def remoteIp() -> str:
        ip = urlopen("https://ident.me").read()
        return ip.decode()


def main():
    try:
        clear()
        print()
        print(colored(figlet_format("INFO"), color="blue"))
        print("\n")
        print(colored("""
[1] Your machine name
[2] Your local ip
[3] Website ip
[4] Your remote ip
[99] Exit
    """, color="blue"))
        yourChoices = int(input(colored("[?] Choose :", color="blue")))
        print("\n")
        if yourChoices == 1:
            print(colored(f"[+] Your Machine Name Is: {InfoGathering.machineName()}", color="blue"))
        elif yourChoices == 2:
            print(colored(f"[+] Your Local IP: {InfoGathering.localIp()}", color="blue"))
        elif yourChoices == 3:
            webSite = str(input(colored("[?] WebSite Domain :", color="blue")))
            print(colored(f"[+] The WebSite IP: {InfoGathering.websiteIp(webSite)}", color="blue"))
        elif yourChoices == 4:
            print(colored(f"[+] The Remote IP: {InfoGathering.remoteIp()}", color="blue"))
        elif yourChoices == 99:
            sys.exit()
        else:
            print(colored("[!] ERROR CHOICES", color="red"))
    except Exception as er:
        print(colored(er, color="red"))
        sys.exit()


if __name__ == '__main__':
    main()
