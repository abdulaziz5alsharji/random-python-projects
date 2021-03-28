try:
    from pyfiglet import figlet_format
    from termcolor import colored
    from pafy import new
    from pytube import Playlist
except Exception as error:
    import sys
    print(error)
    input("Press Any Key To Exit ..")
    sys.exit()

print(colored(figlet_format("YOUTUBE download"), color="blue"))
print(colored("CODING by 5ab_f", color="blue"))
print("\n")
print(colored("[+]Video download \n[+]Audio download \n[+]Info video \n[+]Video PlayList download", color="blue"))


def video_download(url):
    video = new(url)
    if len(video.streams) == 1:
        path_video = input("Video Path==>")
        video.streams[0].download(filepath=path_video)
    else:
        print("Video Quality....")
        print("[+]640x360p \n[+]1280x720 \n[+]Full Quality")
        quality_choose = int(input("Enter your choose==>"))
        if quality_choose == 1:
            path_video = input("Video Path==>")
            video.streams[0].download(filepath=path_video)
        elif quality_choose == 2:
            path_video = input("Video Path==>")
            video.streams[1].download(filepath=path_video)
        elif quality_choose == 3:
            path_video = input("Video Path==>")
            dl = video.getbest()
            dl.download(filepath=path_video)
        else:
            print("you have to choose 1 or 2 or 3...")


def audio_download(url):
    audio = new(url)
    if len(audio.streams) == 1:
        path_audio = input("Audio Path==>")
        audio.streams[0].download(filepath=path_audio)
    else:
        print("Audio Quality....")
        print("[+]640x360p \n[+]1280x720 \n[+]Full Quality")
        quality_choose = int(input("Enter your choose==>"))
        if quality_choose == 1:
            path_audio = input("Audio Path==>")
            audio.audiostreams[0].download(filepath=path_audio)
        elif quality_choose == 2:
            path_audio = input("Audio Path==>")
            audio.audiostreams[1].download(filepath=path_audio)
        elif quality_choose == 3:
            path_audio = input("Audio Path==>")
            dl = audio.getbestaudio()
            dl.download(filepath=path_audio)
        else:
            print("you have to choose 1 or 2 or 3....")


def video_info(url):
    v = new(url)
    print(f"The Video Title Is :{v.title}")
    print(f"The Channel Name Is: {v.author}")
    print(f"The Video Views Is: {v.viewcount}")
    print(f"The Video Likes Is: {v.likes}")
    print(f"The Video Dislikes Is:{v.dislikes}")
    print(f"The Video Time Is: {v.duration}")
    print(f"The Video Image Is: {v.thumb}")
    print(f"The Video ID Is: {v.videoid}")
    print(f"The Video UserName Is: {v.username}")


def VideoPlayList(url):
    video_play_list = Playlist(url)
    print("Videos Quality....")
    print("[+]Full Quality \n[+]low Quality")
    quality_choose = int(input("Enter your choose==>"))
    if quality_choose == 1:
        path = input("Path==>")
        for video in video_play_list.videos:
            video.streams.get_highest_resolution().download(output_path=path)

    elif quality_choose == 2:
        path = input("Path==>")
        for video in video_play_list.videos:
            video.streams.get_lowest_resolution().download(output_path=path)
    else:
        print("you have to choose 1 or 2 or 3....")


try:
    choice = int(input("Type your Choose==>"))
    if choice == 1:
        link_video = input("Type the video link :")
        video_download(link_video)
    elif choice == 2:
        link_video = input("Type the video link :")
        audio_download(link_video)
    elif choice == 3:
        link_video = input("Type the video link :")
        video_info(link_video)
    elif choice == 4:
        link_videos = input("Type the playlist link :")
        VideoPlayList(link_videos)
    else:
        print("You Have To Choice 1 or 2 or 3 .....+_+")
except ValueError:
    print("You have Error...")
except:
    print("Error")
