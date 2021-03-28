import sys

try:
    import qrcode
    from termcolor import colored
    from pyfiglet import figlet_format
except ModuleNotFoundError as error:
    print(error)
    input(colored("Press Any Key To Exit ..", color="red"))
    sys.exit()


class UrlToQrcode:
    def __init__(self, url: str, image_name: str, fill_color="black", background_color="white") -> None:
        self.url = url
        self.fill_color = fill_color
        self.image_name = image_name
        self.background_color = background_color
        # self.conversion()

    def conversion(self) -> None:
        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(self.url)
            qr.make(fit=True)
            image = qr.make_image(fill_color=self.fill_color, back_color=self.background_color)
            image.save(self.image_name)
        except Exception as e:
            print(colored(e, color="red"))
            sys.exit()


if __name__ == '__main__':
    print()
    print(colored(figlet_format("QRCODE"), color="blue"))
    print(colored("Coding By insta @5a_f", color="red"))
    print()
    ULR = input(colored("[?]Enter The URL >", color="green"))
    IMG_NAME = input(colored("[?]Enter The Image Name >", color="green"))
    FILL_COLOR = input(colored("[?]Enter The Fill Color >", color="green"))
    BACKGROUND_COLOR = input(colored("[?]Enter The Background Color >", color="green"))

    UrlToQrcode(
                url=ULR,
                image_name=IMG_NAME,
                fill_color=FILL_COLOR,
                background_color=BACKGROUND_COLOR
                ).conversion()
    print(colored("DONE :)", color="blue"))
