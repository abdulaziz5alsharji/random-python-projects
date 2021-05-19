import sys

try:
    import os
    from platform import system
    from pyfiglet import figlet_format
    from termcolor import colored
    from PIL import Image
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!]Press Any Key To Exit ..", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def convertImageToBlackAndWhite(image_name: str, output_name: str) -> None:
    try:
        image = Image.open(image_name)
        newImage = image.convert("L")
        newImage.save(output_name)
        newImage.show()
    except Exception as er:
        print(colored(er, color="red"))


if __name__ == '__main__':
    clear()
    print()
    print(colored(figlet_format("Convert Image"), color="blue"))
    print("\n")
    imageName = input(colored("[+]Image Name (example.png): ", color="blue"))
    outputName = input(colored("[+]Output Name (example.png): ", color="blue"))
    convertImageToBlackAndWhite(
        image_name=imageName,
        output_name=outputName
    )
    print("\n")
    print(colored(f"[+]DONE >> {outputName}", color="blue"))
