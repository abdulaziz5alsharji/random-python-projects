try:
    from os import system
    from pyfiglet import figlet_format
except ModuleNotFoundError as e:
    import sys

    print(e)
    input("Enter to exit..")
    sys.exit()


class InstagramDownload:
    def __init__(self):
        print(figlet_format("Instagram Downloader "))
        print("\n")
        print("""
[+]Post Download
[+]All Profile Download without igtv (NOT PRIVET)
[+]All Profile Download with igtv (NOT PRIVET)\n
coding by @5ab_f (+_+)
        """)
        self.choice()

    def choice(self):
        try:
            choose = int(input("Enter your Choice -->"))
            print("\n")
            if choose == 1:
                link = input("Type post link :")
                self.post(link)
            elif choose == 2:
                user = input("USER :")
                self.profile(user)
            elif choose == 3:
                user = input("USER :")
                self.alligtv(user)
            else:
                print("PLZ Just Choice (1) or (2) or (3)")
        except ValueError as error:
            print(error)

    def post(self, post_link):
        id_post = post_link[28:39]
        system(f"instaloader -- -{id_post}")
        print("Download Done..")

    def profile(self, user):
        system(f"instaloader profile {user}")
        print("Download Done..")

    def alligtv(self, user):
        system(f"instaloader --igtv {user}")
        print("Download Done..")


InstagramDownload()
