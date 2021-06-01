import sys

try:
    import os
    from platform import system
    from pyfiglet import figlet_format
    from termcolor import colored
    from selenium import webdriver
    from time import sleep
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!]Press Any Key To Exit ..", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


class Automations:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.url = ""

    def githubLogin(self, username: str, password: str) -> None:
        self.driver.get("https://github.com/login")
        self.driver.find_element_by_xpath("/html/body/div[3]/main/div/div[4]/form/input[2]").send_keys(username)
        self.driver.find_element_by_xpath("/html/body/div[3]/main/div/div[4]/form/div/input[1]").send_keys(password)
        self.driver.find_element_by_xpath("/html/body/div[3]/main/div/div[4]/form/div/input[12]").click()

    def createRepository(self, repository_name: str, description: str) -> None:
        sleep(2)
        self.driver.get("https://github.com/new")
        self.driver.find_element_by_xpath("/html/body/div[4]/main/div/form/div[2]/auto-check/dl/dd/input").send_keys(
            repository_name)
        self.driver.find_element_by_xpath("/html/body/div[4]/main/div/form/div[4]/dl/dd/input").send_keys(description)
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[4]/main/div/form/div[4]/button").click()
        sleep(2)
        repositoryUrl = self.driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/git-clone-help/div["
                                                          "1]/div/div[4]/div/span/input")
        self.url = repositoryUrl.get_attribute("value")

    def downloadRepository(self, path) -> None:
        os.chdir(path)
        os.system(f"git clone {self.url}")


if __name__ == '__main__':
    try:
        clear()
        print()
        print(colored(figlet_format("GitHub Automation"), color="blue"))
        print("\n")
        USERNAME = input(colored("[+]Username: ", color="blue"))
        PASS = input(colored("[+]Password: ", color="blue"))
        repositoryName = input(colored("[+]Repository Name: ", color="blue"))
        DESCRIPTION = input(colored("[+]Description: ", color="blue"))
        PATH = input(colored("[+]Path: ", color="blue"))
        print("\n")
        browser = webdriver.Chrome()
        auto = Automations(browser)
        auto.githubLogin(username=USERNAME, password=PASS)
        auto.createRepository(repository_name=repositoryName, description=DESCRIPTION)
        auto.downloadRepository(path=PATH)
    except Exception as er:
        print(colored(er, color="red"))
        sys.exit()
