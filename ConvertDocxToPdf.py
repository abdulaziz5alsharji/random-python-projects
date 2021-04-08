# install package pip install docx2pdf
import sys

try:
    import os
    from docx2pdf import convert
    from platform import system
    from pyfiglet import figlet_format
    from termcolor import colored
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input("Press Any Key To Exit ....")
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


class ConvertDocxToPdf:
    def __init__(self, docx_file: str, pdf_name: str) -> None:
        self.docx_file = docx_file
        self.pdf_name = pdf_name

    def convert_docx_to_pdf(self) -> None:
        try:
            convert(self.docx_file, self.pdf_name)
        except Exception as e:
            print(colored(e, color="red"))
            sys.exit()


if __name__ == '__main__':
    try:
        clear()
        print()
        print(colored(figlet_format("DOCX TO PDF"), color="blue"))
        print("\n")
        DocxFile = input(colored("[?]Docx File >>", color="blue"))
        PdfName = input(colored("[?]Pdf Name >>", color="blue"))
        print()
        file = ConvertDocxToPdf(
            docx_file=DocxFile,
            pdf_name=PdfName
        )
        file.convert_docx_to_pdf()
        print()
        print(colored("[+]Done", color="red"))
    except Exception as er:
        print(colored(er, color="red"))
        sys.exit()


