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


def upload_image(user: str, pass_: str, image_path: str, description="Bot python") -> None:
    try:
        bot = Bot()
        bot.login(username=user, password=pass_)
        bot.upload_photo(photo=image_path, caption=description)
    except Exception as e:
        print(colored(e, color="red"))
        sys.exit()


if __name__ == '__main__':
    try:
        clear()
        print()
        print(colored(figlet_format("InstaBot"), color="blue"))
        print("\n")
        username = input(colored("[?]USERNAME>>", color="green"))
        password = input(colored("[?]PASSWORD>>", color="green"))
        image = input(colored("[?]IMAGE PATH>>", color="green"))
        caption = input(colored("[?]DESCRIPTION>>", color="green"))
        upload_image(
            user=username,
            pass_=password,
            image_path=image,
            description=caption
        )
    except Exception as er:
        print(colored(er, color="red"))
        sys.exit()


