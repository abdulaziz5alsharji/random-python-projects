import sys

try:
    import os
    from platform import system
    from pyfiglet import figlet_format
    from termcolor import colored
    from imdb import IMDb
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!]Press Any Key To Exit ..", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def topMovies(num_movies: int) -> None:
    ia = IMDb()
    search = ia.get_top250_movies()

    for index_ in range(num_movies):
        if index_ == 250:
            break
        print(colored(f"{search[index_]}", color="blue"))


if __name__ == '__main__':
    clear()
    print()
    print(colored(figlet_format("Top Movies"), color="blue"))
    print("\n")
    numberOfMovies = int(input(colored("[+]Number Of Movies: ", color="blue")))
    print(colored("[-]SEARCHING....", color="blue"))
    print("\n")
    topMovies(numberOfMovies)
