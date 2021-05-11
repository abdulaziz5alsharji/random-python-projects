import sys

try:
    import os
    from platform import system
    from moviepy.editor import VideoFileClip
    from termcolor import colored
    from pyfiglet import figlet_format
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!]Press Any Key To Exit ..", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def convertVideoToGif(video_name: str, output_name: str) -> None:
    try:
        video = VideoFileClip(video_name)
        video.write_gif(output_name, fps=10)
    except Exception as er:
        print(colored(er, color="blue"))
        sys.exit()


if __name__ == '__main__':
    clear()
    print()
    print(colored(figlet_format("Convert Video To Gif"), color="blue"))
    print("\n")
    videoName = input(colored("[+]Video Name: ", color="blue"))
    outPutName = input(colored("[+]Output Name: ", color="blue"))
    print("")
    convertVideoToGif(
        video_name=videoName,
        output_name=outPutName)
    print(colored(f"[+]DONE: {outPutName}", color="blue"))
