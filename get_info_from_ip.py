import sys

try:
    import os
    import requests
    from platform import system
    from pyfiglet import figlet_format
    from termcolor import colored
except Exception as error:
    print(colored(error, color="red"))
    input(colored("[+]Press Any Key To Exit ..", color="red"))
    sys.exit()

# To Clean The Terminal
clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def getInfoFromIp(ip: str) -> dict:
    response = requests.get(
        f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,mobile,proxy,hosting,query")
    return response.json()


if __name__ == '__main__':
    clear()
    print()
    print(colored(figlet_format("GET INFO FROM IP"), color="blue"))
    print("\n")
    remoteIp = input(colored("[+]Remote IP: ", color="blue"))
    print("\n")
    for key, value in getInfoFromIp(remoteIp).items():
        print(colored(f"[+]{key}: {value}", color="blue"))


