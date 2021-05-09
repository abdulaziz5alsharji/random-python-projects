import sys

try:
    import os
    from platform import system
    from pyfiglet import figlet_format
    from termcolor import colored
    from googlesearch import search
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!]Press Any Key To Exit ...", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def Search(keyword: str, stop: int, file_name="result_search.txt") -> None:
    try:
        print(colored(f"[+]START SEARCH", color="blue"))
        with open(file_name, "a") as file:
            for result in search(keyword, num_results=stop):
                print(colored(result, color="blue"))
                file.write(result + "\n")
        print(colored(f"[+]END SEARCH  > {file_name}", color="blue"))
    except Exception as e:
        print(colored(e, color="red"))
        sys.exit()


def main():
    clear()
    print()
    print(colored(figlet_format("SEARCHING"), color="blue"))
    print("\n")
    dork = input(colored("[-]DORK: ", color="blue"))
    numOfResult = int(input(colored("[-]NUMBER OF RESULTS: ", color="blue")))
    fileName = input(colored("[-]File Name (end with .txt example.txt): ", color="blue"))
    Search(keyword=dork, stop=numOfResult, file_name=fileName)


if __name__ == '__main__':
    main()
