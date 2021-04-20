import sys

try:
    import os
    from platform import system
    from pyfiglet import figlet_format
    from termcolor import colored
    from pafy import new
    from pytube import Playlist
except Exception as error:
    print(colored(error, color="red"))
    input(colored("[+]Press Any Key To Exit ..", color="red"))
    sys.exit()

# To Clean The Terminal
clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


# Start Class
class YoutubeDownloader:
    def __init__(self, url: str) -> None:
        self.url = url

    # Video Download Method
    def videoDownload(self) -> None:
        try:
            video = new(self.url)
            if len(video.streams) == 1:
                path_video = input(colored("[?]Video Path >>", color="blue"))
                video.streams[0].download(filepath=path_video)
            else:
                print(colored("[+]Video Quality....", color="blue"))
                print("\n")
                print(colored("[+]640x360p \n[+]1280x720 \n[+]Full Quality", color="blue"))
                print()
                quality_choose = int(input(colored("[?]Enter your choice >>", color="blue")))
                if quality_choose == 1:
                    path_video = input(colored("[?]Video Path >>", color="blue"))
                    video.streams[0].download(filepath=path_video)
                elif quality_choose == 2:
                    path_video = input(colored("[?]Video Path >>", color="blue"))
                    video.streams[1].download(filepath=path_video)
                elif quality_choose == 3:
                    path_video = input(colored("[?]Video Path >>", color="blue"))
                    dl = video.getbest()
                    dl.download(filepath=path_video)
                else:
                    print(colored("[-]You Have To Choice 1 or 2 or 3 ", color="red"))
        except Exception as e:
            print("\n")
            print(colored(e, color="red"))
            sys.exit()

    # audio Download Method
    def audioDownload(self) -> None:
        try:
            audio = new(self.url)
            if len(audio.streams) == 1:
                path_audio = input(colored("[?]Audio Path >>", color="blue"))
                audio.streams[0].download(filepath=path_audio)
            else:
                print(colored("[+]Video Quality....", color="blue"))
                print("\n")
                print(colored("[+]640x360p \n[+]1280x720 \n[+]Full Quality", color="blue"))
                print()
                quality_choose = int(input(colored("[?]Enter your choice >>", color="blue")))
                if quality_choose == 1:
                    path_audio = input(colored("[?]Audio Path >>", color="blue"))
                    audio.audiostreams[0].download(filepath=path_audio)
                elif quality_choose == 2:
                    path_audio = input(colored("[?]Audio Path >>", color="blue"))
                    audio.audiostreams[1].download(filepath=path_audio)
                elif quality_choose == 3:
                    path_audio = input(colored("[?]Audio Path >>", color="blue"))
                    dl = audio.getbestaudio()
                    dl.download(filepath=path_audio)
                else:
                    print(colored("[-]You Have To Choice 1 or 2 or 3 ", color="red"))
        except Exception as e:
            print("\n")
            print(colored(e, color="red"))
            sys.exit()

    # PlayList Download Method
    def videoPlayList(self) -> None:
        try:
            video_play_list = Playlist(self.url)
            print(colored("[+]Video Quality....", color="blue"))
            print("\n")
            print(colored("[+]Full Quality \n[+]low Quality", color="blue"))
            print()
            quality_choose = int(input(colored("[?]Enter your choice >>", color="blue")))
            if quality_choose == 1:
                path = input(colored("[?]Path >>", color="blue"))
                for video in video_play_list.videos:
                    video.streams.get_highest_resolution().download(output_path=path)

            elif quality_choose == 2:
                path = input(colored("[?]Path >>", color="blue"))
                for video in video_play_list.videos:
                    video.streams.get_lowest_resolution().download(output_path=path)
            else:
                print(colored("[+]you have to choose 1 or 2 or 3....", color="red"))
        except Exception as e:
            print("\n")
            print(colored(e, color="red"))
            sys.exit()

    # Video Info Method
    def videoInfo(self) -> None:
        try:
            video = new(self.url)
            print(colored(f"[+]The Video Title Is :{video.title}", color="blue"))
            print(colored(f"[+]The Channel Name Is: {video.author}", color="blue"))
            print(colored(f"[+]The Video Views Is: {video.viewcount}", color="blue"))
            print(colored(f"[+]The Video Likes Is: {video.likes}", color="blue"))
            print(colored(f"[+]The Video Dislikes Is:{video.dislikes}", color="blue"))
            print(colored(f"[+]The Video Time Is: {video.duration}", color="blue"))
            print(colored(f"[+]The Video Image Is: {video.thumb}", color="blue"))
            print(colored(f"[+]The Video ID Is: {video.videoid}", color="blue"))
            print(colored(f"[+]The Video UserName Is: {video.username}", color="blue"))
        except Exception as e:
            print("\n")
            print(colored(e, color="red"))
            sys.exit()


# The Main Function
def main():
    try:
        clear()
        print(colored(figlet_format("Youtube Downloader </>"), color="blue"))
        print("\n")
        print(colored("""
[+]Video download
[+]Audio download
[+]Video PlayList download
[+]Info video
        """, color="blue"))
        print("\n")
        choice = int(input(colored("[?]Enter your choice >>", color="blue")))
        URl = input(colored("[?]Video URL >>", color="blue"))
        Youtube = YoutubeDownloader(url=URl)
        if choice == 1:
            Youtube.videoDownload()
            print("\n")
            print(colored("[+]DONE </>", color="blue"))
        elif choice == 2:
            Youtube.audioDownload()
            print("\n")
            print(colored("[+]DONE </>", color="blue"))
        elif choice == 3:
            Youtube.videoPlayList()
            print("\n")
            print(colored("[+]DONE </>", color="blue"))
        elif choice == 4:
            Youtube.videoInfo()
        else:
            print(colored("[-]You Have To Choice 1 or 2 or 3 ", color="red"))
    except Exception as e:
        print("\n")
        print(colored(e, color="red"))
        sys.exit()


if __name__ == '__main__':
    main()
