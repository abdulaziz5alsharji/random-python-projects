try:
    from urllib.request import urlretrieve
    from pyfiglet import figlet_format
    from termcolor import colored
    import urllib.error
except Exception as e:
    import sys

    print(e)
    input("Press to exit..")
    sys.exit()


class ImageDownloader:
    def __init__(self):
        self.done = 1
        print(colored(figlet_format("Image Downloader"), color="blue"))
        self.mode()

    def mode(self):
        print("""
[+]Download Images (1)
[+]Download Image (2)
        """)
        self.choices = int(input("[?]Enter Your Choose >>"))
        if self.choices == 1:
            self.download_images()
        elif self.choices == 2:
            self.download_image()

    def download_image(self):
        try:
            self.url = input("Enter the image url >>")
            self.image_name = input("[?]Enter The Image Name >>")
            self.extension = input("[?]Enter The Image Extension >>")
            urlretrieve(self.url, f"{self.image_name}.{self.extension}")
            print("[+]Download Done +_+")
        except urllib.error.HTTPError as error_1:
            print(error_1)
        except Exception as error_2:
            print(error_2)

    def download_images(self):
        try:
            self.file = input("[?]Enter the file image urls >>")
            self.file_urls = open(self.file, "r").read().split("\n")
            self.image_name = input("[?]Enter The Image Name >>")
            self.extension = input("[?]Enter The Image Extension >>")
            for url in self.file_urls:
                urlretrieve(url, f"{self.image_name}_{self.done}.{self.extension}")
                self.done += 1
            print("[+]Download Done +_+")
        except urllib.error.HTTPError as error_1:
            print(error_1)
        except Exception as error_2:
            print(error_2)


if __name__ == "__main__":
    ImageDownloader()
