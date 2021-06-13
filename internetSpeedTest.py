import sys

try:
    import os
    import speedtest
    from platform import system
    from pyfiglet import figlet_format
    from termcolor import colored
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!]Press Any Key To Exit .. ", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def internetSpeedTest():
    speedTest = speedtest.Speedtest()
    print(colored("[+]LOADING SERVERS LIST...", color="red"))
    speedTest.get_servers()
    print(colored("[+]CHOOSING BEST SERVER...", color="red"))
    best = speedTest.get_best_server()
    print("\n")
    print(colored(f"[+]FOUND: {best['host']}, LOCATED IN: {best['country']}", color="green"))
    print(colored("[+]PERFORMING DOWNLOAD TEST...", color="green"))
    downloadSpeed = speedTest.download()
    print(colored("[+]PERFORMING UPLOAD TEST...", color="green"))
    uploadSpeed = speedTest.upload()
    ping = speedTest.results.ping
    print("\n")
    print(colored(f"[+]DOWNLOAD SPEED: {downloadSpeed / 1024 / 1024} M bit/s", color="blue"))
    print(colored(f"[+]UPLOAD SPEED: {uploadSpeed / 1024 / 1024} M bit/s", color="blue"))
    print(colored(f"[+]PING: {ping} ms", color="blue"))


if __name__ == '__main__':
    clear()
    print(colored(figlet_format("Internet Speed Test"), color="blue"))
    print("\n")
    internetSpeedTest()
