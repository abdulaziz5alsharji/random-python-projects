import sys

try:
    import os
    from platform import system
    from pyfiglet import figlet_format
    from termcolor import colored
except Exception as error:
    print(colored(error, color="red"))
    input(colored("[+]Press Any Key To Exit ..", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


class IndexMaker:
    def __init__(self, output_path: str) -> None:
        self.path = output_path

    def html(self, title: str, image: str, head: str, paragraph_one: str, paragraph_two: str) -> None:
        content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>{title}</title>
</head>
<body>
    <div class="container">
        <img src="{image}" alt="Hacking">
        <h1>{head}</h1>
        <p>{paragraph_one}</p> 
        <p>{paragraph_two}</p>
    </div>
</body>
</html>
"""
        with open(rf"{self.path}\index.html", "w") as html_index:
            html_index.write(content)

    def css(self, bg: str, img_width: int, head_color: str, paragraph_color: str):
        style = """
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body{
    background-color: %s;
}
.container {
    width: 800px;
    height: 100vh;
    margin: 50px auto;
    text-align: center;
}

img {
    width: %dpx;
    margin-bottom: 30px;
}
h1 {
    text-transform: uppercase;
    color: %s;
    margin-bottom: 20px;

}
p{
    color: %s;
    text-transform: capitalize;
    margin-bottom: 20px;
}        
""" % (bg, img_width, head_color, paragraph_color)

        with open(rf"{self.path}\style.css", "w") as css_style:
            css_style.write(style)


if __name__ == '__main__':
    try:
        clear()
        print()
        print(colored(figlet_format("Index Maker"), color="blue"))
        print("\n")
        PATH = input(colored("[+]Path: ", color="blue"))
        TITLE = input(colored("[+]Index Title: ", color="blue"))
        IMG_PATH = input(colored("[+]Image Path: ", color="blue"))
        HEAD = input(colored("[+]Head: ", color="blue"))
        PARAGRAPH_ONE = input(colored("[+]First Paragraph: ", color="blue"))
        PARAGRAPH_TWO = input(colored("[+]Second Paragraph: ", color="blue"))
        BG_COLOR = input(colored("[+]Background Color: ", color="blue"))
        IMG_WIDTH = int(input(colored("[+]Image Width: ", color="blue")))
        HEAD_COLOR = input(colored("[+]Head Color: ", color="blue"))
        PARAGRAPH_COLOR = input(colored("[+]Paragraph Color: ", color="blue"))
        print("\n")
        indexMaker = IndexMaker(output_path=PATH)
        indexMaker.html(
            title=TITLE,
            image=IMG_PATH,
            head=HEAD,
            paragraph_one=PARAGRAPH_ONE,
            paragraph_two=PARAGRAPH_TWO
        )
        indexMaker.css(
            bg=BG_COLOR,
            img_width=IMG_WIDTH,
            head_color=HEAD_COLOR,
            paragraph_color=PARAGRAPH_COLOR)
        print(colored("[+]DONE...", color="blue"))
    except Exception as er:
        print(colored(er, color="red"))
