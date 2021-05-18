import sys

try:
    import os
    from platform import system
    from pyfiglet import figlet_format
    from termcolor import colored
    from pafy import new
    from urllib.request import urlretrieve
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!]Press Any Key To Exit ..", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


class VideoInfo:
    def __init__(self, url: str) -> None:
        self.url = url

    def getVideoInfo(self) -> dict:
        video = new(self.url)
        info = {
            "title": video.title,
            "author": video.author,
            "duration": video.duration,
            "id": video.videoid,
            "views": video.viewcount,
            "rating": video.rating,
            "thumb": video.bigthumbhd,
            "likes": video.likes,
            "dislikes": video.dislikes,
            "length": video.length,
            "streams": video.streams,
            "category": video.category
        }
        return info

    def downloadVideoImage(self) -> str:
        data = self.getVideoInfo()
        urlretrieve(data["thumb"], f"{data['author']}.png")
        return f"Download DONE: {data['author']}.png"


def videoScraping(link: str) -> VideoInfo:
    return VideoInfo(url=link)


if __name__ == '__main__':
    clear()
    print()
    print(colored(figlet_format("Youtube Scarping"), color="blue"))
    print("\n")
    print(colored("""
[1]Video Info
[2]Video Image Downloading
[99]Exit
""", color="blue"))
    print("\n")
    try:
        option = int(input(colored("[+]Choose: ", color="blue")))
        print("\n")
        if option == 1:
            URL = input(colored("[+]Video Link: ", color="blue"))
            VIDEO = videoScraping(link=URL)
            print(colored("[-]SEARCHING ...", color="red"))
            DATA = VIDEO.getVideoInfo()
            print("\n")
            for key, value in DATA.items():
                print(colored(f"[+]{key}: {value}", color="blue"))
        elif option == 2:
            URL = input(colored("[+]Video Link: ", color="blue"))
            VIDEO = videoScraping(link=URL)
            print(colored("[-]Downloading ...", color="red"))
            print("\n")
            print(colored(VIDEO.downloadVideoImage(), color="blue"))
        elif option == 99:
            sys.exit()
        else:
            print(colored("[!]INVALID OPTION", color="red"))
    except ValueError as er:
        print(colored(er, color="red"))

    except Exception as e:
        print(colored(e, color="red"))

