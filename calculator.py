class Calculator:
    @staticmethod
    def add(x: int, y: int) -> int:
        return x + y

    @staticmethod
    def sub(x: int, y: int) -> int:
        return x - y

    @staticmethod
    def mul(x: int, y: int) -> int:
        return x * y

    @staticmethod
    def div(x: int, y: int) -> int:
        return x // y


def main():
    try:
        print()
        print("WELCOME IN MY CALCULATOR")
        firstNumber = int(input("[-] First Number :"))
        operation = str(input("[-] Operation :"))
        secondNumber = int(input("[-] Second Number :"))
        if operation == "+":
            print()
            print("[+] The Sum is: {} ".format(Calculator.add(firstNumber, secondNumber)))
        elif operation == "-":
            print()
            print("[+] The Sub is: {} ".format(Calculator.sub(firstNumber, secondNumber)))
        elif operation == "x":
            print()
            print("[+] The mul is: {} ".format(Calculator.mul(firstNumber, secondNumber)))
        elif operation == "/":
            print()
            print("[+] The div is: {} ".format(Calculator.div(firstNumber, secondNumber)))
        else:
            print()
            print("[!] Invalid operation")
    except ValueError as error:
        print()
        print(error)


if __name__ == '__main__':
    main()
