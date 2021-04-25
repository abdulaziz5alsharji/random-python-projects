import sys

try:
    import os
    import requests
    from platform import system
    from pyfiglet import figlet_format
    from termcolor import colored
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!] Press Any Key To Exit ..", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def getNews(api_key: str, country: str) -> None:
    try:
        url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}"
        response = requests.get(url)
        articleNumber = 1
        articles = response.json()["articles"]
        if len(articles) == 0:
            print(colored("[!] Not Found Any Article", color="red"))
            sys.exit()
        else:
            for item in articles:
                print("\n")
                print(colored(
                    f" ================================ Article {articleNumber} ================================",
                    color="red"))
                print("\n")
                print(colored(f"[+] The Author is : {item['author']}", color="blue"))
                print()
                print(colored(f"[+] The Title is : {item['title']}", color="blue"))
                print()
                print(colored(f"[+] The Description is : {item['description']}", color="blue"))
                print()
                print(colored(f"[+] The Content is : {item['content']}", color="blue"))
                articleNumber += 1
    except Exception as e:
        print(colored(e, color="red"))
        sys.exit()


def main():
    key = "write here Api key, use this website to get Api Key: https://newsapi.org/"
    clear()
    print()
    print(colored(figlet_format("NEWS"), color="blue"))
    print("\n")
    Country = input(colored("[?]COUNTRY >", color="blue"))
    getNews(
        api_key=key,
        country=Country
    )


if __name__ == '__main__':
    main()
