import sys

try:
    import platform
    import os
    from pyfiglet import figlet_format
    from termcolor import colored
except ModuleNotFoundError as error:
    print(error)
    input("Press Any key To Exit ..")
    sys.exit()


def shutdown(time_with_second=0) -> str:
    if platform.system() == "Windows":
        os.system(f"shutdown -s -t {time_with_second}")
        return f"Start Shutdown {time_with_second}"
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("reboot now")
        return "Shutdown New"
    else:
        return colored("Os not supported!")


def restart() -> str:
    if platform.system() == "Windows":
        os.system("shutdown -t 0 -r -f")
        return "Restart"
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("reboot now")
        return "Restart"
    else:
        return colored("Os not supported!")


def main():
    try:
        print(colored(figlet_format("R $ S"), color="blue"))
        print()
        choices = input(colored("[?]Restart (R) or Shutdown (S) ??", color="blue"))
        if choices.upper() == "R":
            print(restart())
        elif choices.upper() == "S":
            time = int(input(colored("[?]Time(second)>:", color="blue")))
            print(shutdown(time))
        else:
            print(colored("Wrong Letter", color="red"))
    except Exception as e:
        print(colored(e, color="red"))
        sys.exit()


if __name__ == '__main__':
    main()
