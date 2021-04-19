import sys

try:
    import os
    from platform import system
    from pyfiglet import figlet_format
    from termcolor import colored
    from gtts import gTTS
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input("[!]Press Any Key To Exit ..")
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def convertTextToAudio(text: str, lang="en", audio_name="0001.mp3") -> None:
    try:
        tts = gTTS(text, lang=lang)
        tts.save(savefile=audio_name)
        os.system(audio_name)
    except Exception as er:
        print(colored(er, color="red"))
        sys.exit()


if __name__ == '__main__':
    try:
        clear()
        print()
        print(colored(figlet_format("TEXT TO AUDIO"), color="blue"))
        print("\n")
        string = input(colored("[?]Type Text:", color="blue"))
        LANG = input(colored("[?]Enter The Lang:", color="blue"))
        AudioName = input(colored("[?]Enter The Audio Name:", color="blue"))
        convertTextToAudio(
            text=string,
            lang=LANG,
            audio_name=AudioName
        )
        print()
        print(colored("[+]Done </>", color="blue"))
    except Exception as e:
        print(colored(e, color="red"))
        sys.exit()
