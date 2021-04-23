import sys

try:
    import os
    import random
    import requests
    from platform import system
    from pyfiglet import figlet_format
    from termcolor import colored
    from headers import HEADERS
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!] Press Any Key To Exit ..", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


class DarkWeb:
    def __init__(self, keyword: str, pag_number: int) -> None:
        self.keyword = keyword
        self.page_num = pag_number

    def getUrls(self) -> None:
        file_name = "urlsDarkWeb.txt"
        file = open(file_name, "a")
        try:
            url = "https://darksearch.io/api/search"
            params = {
                "query": self.keyword,
                "page": self.page_num

            }
            response = requests.get(url, params=params)
            response.headers["User-Agent"] = random.choice(HEADERS)
            jsonData = response.json()
            if jsonData["total"] == 0:
                print(colored("[-] No results found", color="red"))
            else:
                for page in range(1, self.page_num + 1):
                    print(colored(f"[+]START PAGE NUMBER {page}", color="red"))
                    print("\n")
                    for index_ in range(0, 18):
                        siteTitle = jsonData['data'][index_]['title']
                        siteUrl = jsonData['data'][index_]['link']
                        file.write(siteUrl + "\n")
                        print(colored(f"[+]Title Site: {siteTitle}", color="blue"))
                        print(colored(f"[+]Url Site: {siteUrl}", color="blue"))
                        print("")
                    print("\n")
            print("\n")
            print(colored(f"You Can Find All The Urls In {file_name}", color="green"))
        except Exception as e:
            print(colored(e, color="red"))
            sys.exit()
        finally:
            file.close()


def main():
    try:
        clear()
        print()
        print(colored(figlet_format("DARK WEB SEARCH"), color="blue"))
        print("\n")
        keyWord = str(input(colored("[?] Keyword >", color="blue")))
        pageNumber = int(input(colored("[?] Page number >", color="blue")))
        DarkWeb(keyword=keyWord, pag_number=pageNumber).getUrls()
    except Exception as er:
        print(colored(er, color="red"))
        sys.exit()


if __name__ == '__main__':
    main()
