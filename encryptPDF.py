import sys

try:
    import os
    from platform import system
    from pyfiglet import figlet_format
    from termcolor import colored
    import PyPDF2
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!] Press Any Key To Exit ..", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


def encryptPDF(pdf_name: str, password: str, output="encrypt_pdf.pdf") -> None:
    try:
        pdfReader = PyPDF2.PdfFileReader(pdf_name)
        pdfWriter = PyPDF2.PdfFileWriter()
        for page in range(pdfReader.numPages):
            pdfWriter.addPage(pdfReader.getPage(page))

        pdfWriter.encrypt(password)

        with open(output, "wb") as file:
            pdfWriter.write(file)
    except Exception as e:
        print(colored(e, color="red"))
        sys.exit()


def main():
    clear()
    print("")
    print(colored(figlet_format("Encrypt PDF"), color="blue"))
    print("\n")
    pdfName = input(colored("[?] PDF NAME:", color="blue"))
    PASSWORD = input(colored("[?] PASSWORD:", color="blue"))
    encryptPDF(
        pdf_name=pdfName,
        password=PASSWORD
    )
    print("\n")
    print(colored("[+]DONE </>", color="blue"))


if __name__ == '__main__':
    main()
