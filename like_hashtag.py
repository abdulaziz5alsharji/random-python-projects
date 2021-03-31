import sys

try:
    import os
    from instabot import Bot
    from pyfiglet import figlet_format
    from termcolor import colored
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input("Press Any Key To Exit ..")
    sys.exit()

clear = lambda: os.system("cls")


def like_hash_tag(user: str, pass_: str, hashtag: str, amount=20) -> None:
    try:
        bot = Bot()
        bot.login(username=user, password=pass_)
        bot.like_hashtag(hashtag=hashtag, amount=amount)
    except Exception as e:
        print(colored(e, color="red"))
        sys.exit()


if __name__ == '__main__':
    try:
        clear()
        print()
        print(colored(figlet_format("LINK HASHTAG"), color="blue"))
        print("\n")
        UserName = input(colored("[?]USERNAME >>", color="green"))
        PassWord = input(colored("[?]PASSWORD >>", color="green"))
        HashTag = input(colored("[?]HashTag >>", color="green"))
        Amount = int(input(colored("[?]Amount >>", color="green")))
        like_hash_tag(
            user=UserName,
            pass_=PassWord,
            hashtag=HashTag,
            amount=Amount
        )
    except Exception as er:
        print(colored(er, color="red"))
        sys.exit()
