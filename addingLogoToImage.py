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


def addLogoToImage(logo_name: str, folder_image: str, output_folder: str) -> None:
    Logo = Image.open(logo_name)
    logoWidth, logoHeight = Logo.size
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    os.chdir(folder_image)
    for image in os.listdir(os.getcwd()):
        if image.endswith(("png", "jpg", "jpeg", "gif")) and image != logo_name:
            img = Image.open(image)
            width, height = img.size
            print(colored(f"[++]Adding Logo To {image}", color="green"))
            img.paste(Logo, (width - logoWidth, height - logoHeight), Logo)
            img.save(os.path.join(output_folder, image))
            print(colored("------------------------------", color="green"))

    print("\n")
    print(colored("[++]:::::::::::::::DONE ADD ALL IMAGE:::::::::::::::[++]", color="green"))


if __name__ == '__main__':
    try:
        clear()
        print()
        print(colored(figlet_format("Add Logo To Image"), color="green"))
        print("\n")
        LOGO = str(input(colored("[+]Logo Name: ", color="green")))
        imagesFolder = str(input(colored("[+]Images Folder: ", color="green")))
        outputFolder = str(input(colored("[+]Output Folder: ", color="green")))
        print("\n")
        addLogoToImage(logo_name=LOGO, folder_image=imagesFolder, output_folder=outputFolder)
    except Exception as er:
        print(colored(er, color="red"))
