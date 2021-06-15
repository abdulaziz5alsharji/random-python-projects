import sys

try:
    import os
    from PIL import Image
    from platform import system
    from pyfiglet import figlet_format
    from termcolor import colored
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!]Press Any Key To Exit ....", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def resizeImages(new_size: int, folder_image: str, output_folder: str) -> None:
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    os.chdir(folder_image)
    for image in os.listdir(os.getcwd()):
        if image.endswith(("png", "jpg", "jpeg", "gif")):
            img = Image.open(image)
            width, height = img.size
            if width > new_size and height > new_size:
                if width > height:
                    height = int((new_size / width) * height)
                    width = new_size
                else:
                    width = int((new_size / height) * width)
                    height = new_size
                img.resize((width, height))
                print(colored(f"[++]Resize Done: {image}", color="green"))
                img.save(os.path.join(output_folder, image))
                print(colored("------------------------------", color="green"))
            else:
                print(colored(f"[!!]Small Image: {image}", color="red"))
                print(colored("------------------------------", color="green"))
    print("\n")
    print(colored("[++]:::::::::::::::Resizing Done:::::::::::::::[++]", color="green"))


if __name__ == '__main__':
    try:
        clear()
        print()
        print(colored(figlet_format("Resize Image"), color="green"))
        print("\n")
        imageNewSize = int(input(colored("[+]New Size: ", color="green")))
        imagesFolder = str(input(colored("[+]Images Folder: ", color="green")))
        outputFolder = str(input(colored("[+]Output Folder: ", color="green")))
        print("\n")
        resizeImages(new_size=imageNewSize, folder_image=imagesFolder, output_folder=outputFolder)
    except ValueError as err:
        print(colored(err, color="red"))
    except Exception as er:
        print(colored(er, color="red"))

