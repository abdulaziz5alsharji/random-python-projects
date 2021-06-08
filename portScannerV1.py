import sys

try:
    import os
    import socket
    from datetime import datetime
    from platform import system
    from pyfiglet import figlet_format
    from termcolor import colored
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input("Press Any Key To Exit ....")
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def portScanner(target: str, start: int, end: int) -> None:
    try:
        socketObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        for port in range(start, end + 1):
            connection = socketObject.connect_ex((target, port))
            if connection == 0:
                print(colored(f"[+]Port {port} Is Open", color="blue"))
            else:
                print(colored(f"[+]Port {port} Is Close", color="red"))
    except KeyboardInterrupt:
        print(colored("Exit Program !!!!", color="red"))
        sys.exit()
    except socket.gaierror:
        print(colored("Hostname Could Not Be Resolved !!!!", color="red"))
        sys.exit()
    except socket.error:
        print(colored("Server not responding !!!!", color="red"))
        sys.exit()


if __name__ == '__main__':
    try:
        clear()
        print()
        print(colored(figlet_format("Port Scanner"), color="blue"))
        print("\n")
        HOST = input(colored("[+]Host or Ip: ", color="blue"))
        Start = int(input(colored("[+]Start: ", color="blue")))
        End = int(input(colored("[+]End: ", color="blue")))
        print("\n")
        print(colored(f"[+]Start Scan: {datetime.now().time()} || {datetime.now().date()}", color="green"))
        print()
        portScanner(target=HOST, start=Start, end=End)
    except ValueError as er:
        print(colored(er, color="red"))
