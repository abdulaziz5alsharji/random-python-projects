import sys

try:
    from instabot import Bot
    from pyfiglet import figlet_format
    from termcolor import colored
    import os
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input("Press Any Key To Exit ..")
    sys.exit()

clear = lambda: os.system("cls")


def instagram_follow(user: str, pass_: str, target: str, follow_number: int) -> None:
    try:
        bot = Bot()
        bot.login(username=user, password=pass_)
        bot.follow_followers(user_id=target, nfollows=follow_number)
    except Exception as e:
        print(colored(e,color="red"))
        sys.exit()


if __name__ == '__main__':
    try:
        clear()
        print()
        print(colored(figlet_format("InstaBot"), color="blue"))
        print("\n")
        username = input(colored("[?]USERNAME>>", color="green"))
        password = input(colored("[?]PASSWORD>>", color="green"))
        TARGET = input(colored("[?]TARGET>>", color="green"))
        FollowNumber = int(input(colored("[?]FOLLOWS NUMBER>>", color="green")))
        instagram_follow(
            user=username,
            pass_=password,
            target=TARGET,
            follow_number=FollowNumber
        )
    except Exception as er:
        print(colored(er, color="red"))
        sys.exit()
