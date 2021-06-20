import sys

try:
    import os
    import time
    from selenium import webdriver
    from urllib.request import urlretrieve
    from termcolor import colored
    from pyfiglet import figlet_format
    from platform import system
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!]Press Any Key To Exit...", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


class GoogleAutomation:
    def __init__(self, driver) -> None:
        self.browser = driver

    def searchGoogle(self, keyword: str) -> None:
        self.browser.get("https://www.google.com")
        time.sleep(1)
        self.browser.find_element_by_xpath(
            "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(keyword)
        self.browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("/html/body/div[7]/div/div[4]/div/div[1]/div/div[1]/div/div[2]/a").click()

    def downloadImages(self, path: str, limit: int) -> None:
        try:
            time.sleep(1)
            images = self.browser.find_elements_by_tag_name("img")
            for counter in range(limit):
                urlretrieve(images[counter].get_attribute("src"), fr"{path}\{counter + 1}.png")
                print(colored(f"\rDONE: {counter + 1}", color="green"), end="")
        except Exception as er:
            print(colored(er, color="red"))


if __name__ == '__main__':
    try:
        clear()
        print()
        print(colored(figlet_format("Google Automation"), color="blue"))
        print("\n")
        Keyword = input(colored("[++]Keyword: ", color="blue"))
        Path = input(colored("[++]Path: ", color="blue"))
        Limit = int(input(colored("[++]Limit: ", color="blue")))
        print("\n")
        browser = webdriver.Chrome()
        google = GoogleAutomation(browser)
        google.searchGoogle(keyword=Keyword)
        google.downloadImages(path=Path, limit=Limit)
        print("\n")
        print(colored("[==]================ DONE ALL ==================[==]", color="blue"))
    except Exception as err:
        print(colored(err, color="red"))
