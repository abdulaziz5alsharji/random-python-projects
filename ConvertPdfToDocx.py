import sys

try:
    import os
    from pdf2docx import Converter
    from pyfiglet import figlet_format
    from termcolor import colored
    from platform import system
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input("Press Any Key To Exit ..")
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


class ConvertPdfToDocx:
    def __init__(self, pdf_file: str, docx_name: str) -> None:
        self.pdf_file = pdf_file
        self.docx_name = docx_name

    def convert(self, start=0, end=None) -> None:
        try:
            file = Converter(self.pdf_file)
            file.convert(self.docx_name, start=start, end=end)
            file.close()
        except Exception as er:
            print(colored(er, color="red"))
            sys.exit()


if __name__ == '__main__':
    try:
        clear()
        print()
        print(colored(figlet_format("PDF TO DOCX"), color="blue"))
        print("\n")
        PdfFile = input(colored("[?]PDF File >>", color="blue"))
        DocxName = input(colored("[?]Docx Name >>", color="blue"))

        cv = ConvertPdfToDocx(
            pdf_file=PdfFile,
            docx_name=DocxName)
        cv.convert()
        print(colored("[+]DONE</>", color="blue"))
    except Exception as e:
        print(colored(e, color="red"))
        sys.exit()


