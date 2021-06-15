import sys

try:
    import os
    import shutil
    from platform import system
    from pyfiglet import figlet_format
    from termcolor import colored
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!]Press Any Key To Exit ....", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")

imageExtension = ("png", "jpg", "jpeg", "gif", "ico")
videoExtension = ("mp4", "webm", "mov", "wmv", "avi", "mkv")
codeExtension = ("py", "html", "css", "js", "php", "cpp", "bat", "c", "vb")
audioExtension = ("mp3", "ogg", "aac")
docExtension = ("pdf", "docx", "xlsx", "accdb", "pptx")
appExtension = ("dmg", "exe")
archiveExtension = ("zip", "rar")
textExtension = "txt"


def organizeYourFiles(path: str) -> None:
    os.chdir(path)
    currentDir = os.getcwd()
    for filename in os.listdir(currentDir):
        if filename.endswith(imageExtension):
            if not os.path.exists("Images"):
                os.mkdir("Images")
            shutil.copy(filename, "Images")
            os.remove(filename)
            print(colored(f"[+]Done {filename}", color="blue"))

        elif filename.endswith(videoExtension):
            if not os.path.exists("Videos"):
                os.mkdir("Videos")
            shutil.copy(filename, "Videos")
            os.remove(filename)
            print(colored(f"[+]Done {filename}", color="blue"))

        elif filename.endswith(audioExtension):
            if not os.path.exists("Audios"):
                os.mkdir("Audios")
            shutil.copy(filename, "Audios")
            os.remove(filename)
            print(colored(f"[+]Done {filename}", color="blue"))

        elif filename.endswith(codeExtension):
            if not os.path.exists("Codes"):
                os.mkdir("Codes")
            shutil.copy(filename, "Codes")
            os.remove(filename)
            print(colored(f"[+]Done {filename}", color="blue"))

        elif filename.endswith(docExtension):
            if not os.path.exists("Docs"):
                os.mkdir("Docs")
            shutil.copy(filename, "Docs")
            os.remove(filename)
            print(colored(f"[+]Done {filename}", color="blue"))

        elif filename.endswith(appExtension):
            if not os.path.exists("Apps"):
                os.mkdir("Apps")
            shutil.copy(filename, "Apps")
            os.remove(filename)
            print(colored(f"[+]Done {filename}", color="blue"))

        elif filename.endswith(archiveExtension):
            if not os.path.exists("Archives"):
                os.mkdir("Archives")
            shutil.copy(filename, "Archives")
            os.remove(filename)
            print(colored(f"[+]Done {filename}", color="blue"))

        elif filename.endswith(textExtension):
            if not os.path.exists("Texts"):
                os.mkdir("Texts")
            shutil.copy(filename, "Texts")
            os.remove(filename)
            print(colored(f"[+]Done {filename}", color="blue"))

        else:
            print(colored(f"[!]Not Found {filename}", color="red"))

    print("\n")
    print(colored("[++]DONE ALL", color="blue"))


if __name__ == '__main__':
    clear()
    print()
    print(colored(figlet_format("Folder Organizer"), color="blue"))
    print("\n")
    folderPath = input(colored("[+]Folder Path: ", color="blue"))
    print("\n")
    organizeYourFiles(path=folderPath)
