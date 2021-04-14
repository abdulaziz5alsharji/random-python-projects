import sys

try:
    import os
    from platform import system
    import moviepy.editor
    from pyfiglet import figlet_format
    from termcolor import colored
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input("[+]Press Any Key To Exit ..")
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def extract_audio_from_video(video_name: str, audio_name: str) -> None:
    try:
        video = moviepy.editor.VideoFileClip(video_name)
        audio = video.audio
        audio.write_audiofile(audio_name)
    except Exception as er:
        print(colored(er, color="red"))
        sys.exit()


if __name__ == '__main__':
    try:
        clear()
        print()
        print(colored(figlet_format("Extract Audio"), color="blue"))
        print("\n")
        VideoName = input(colored("[?]Video Name >>", color="blue"))
        AudioName = input(colored("[?]Audio Name >>", color="blue"))
        print()
        extract_audio_from_video(
            video_name=VideoName,
            audio_name=AudioName)
    except Exception as e:
        print(colored(e, color="red"))
        sys.exit()
