import sys

try:
    import requests
    from bs4 import BeautifulSoup
    from urllib.request import urlretrieve
    from termcolor import colored
    from pyfiglet import figlet_format
except ModuleNotFoundError as error:
    print("error")
    input("Press Any Key To Exit ..")
    sys.exit()


def get_profile_image(username: str) -> str:
    try:
        url = f"https://github.com/{username}"
        github_req = requests.get(url)
        content = github_req.text
        soup = BeautifulSoup(content, "lxml")
        return soup.find("img", {"class": "avatar avatar-user width-full border color-bg-primary"}).get("src")
    except Exception as e:
        print(colored(e, color="red"))
        print(colored("NOT FOUND", color="red"))
        sys.exit()


def download_image(url: str, image_name: str, extension="png"):
    try:
        image = urlretrieve(url, f"{image_name}.{extension}")
        return image
    except Exception as download_error:
        print(colored(download_error, color="red"))
        sys.exit()


if __name__ == '__main__':
    print(colored(figlet_format("GitHub"), color="blue"))
    print()
    target = input(colored("[?]Enter The UserName Target >>", color="blue"))
    print(colored(f"IMAGE LINK : {get_profile_image(username=target)}", color="green"))
    choose = input(colored("[?]Do you want to download image (Y) or (N) >>", color="blue"))
    if choose.upper() == "Y":
        ImageName = input(colored("[?]Type Image Name >>", color="blue"))
        print(colored(download_image(get_profile_image(username=target), ImageName), color="green"))
        print(colored("[$] Download Done", color="green"))
    elif choose.upper() == "N":
        sys.exit()
    else:
        print(colored("PLZ Choose (N) or (Y)", color="red"))
