import sys

try:
    import os
    import requests
    from platform import system
    from termcolor import colored
    from pyfiglet import figlet_format
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[+]Press Any Key To Exit .. ", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def tikTopDownloader(url: str, video_name: str) -> None:
    try:
        URL = f"https://hamod.ga/api/tiktokWithoutWaterMark.php?u={url}"
        response = requests.get(URL).json()
        link = response["link"]
        if link is None:
            print(colored("[!!]NOT FOUND, Click The Link[!!]", color="red"))
        else:
            print(colored("[++]START Downloading[++]", color="blue"))
            videoContent = requests.get(link).content
            with open(video_name, "wb") as video:
                video.write(videoContent)
            print(colored(f"[++]Done Download, {video_name}[++]", color="blue"))
    except Exception as er:
        print(colored(er, color="red"))
        input(colored("[+]Press Any Key To Exit .. ", color="red"))
        sys.exit()


if __name__ == '__main__':
    clear()
    print()
    print(colored(figlet_format("TikTok Downloader"), color="blue"))
    print("\n")
    VIDEO_LINK = input(colored("[++]Video Link: ", color="blue"))
    VIDEO_NAME = input((colored("[++]Video Name (example.mp4): ", color="blue")))
    print("\n")
    tikTopDownloader(VIDEO_LINK, video_name=VIDEO_NAME)


