import re
from random import choice
from menu.menuTexts import lengthMenuText, enterBinaryText, getBinaryText


def is_binary(value):
    binary_pattern = re.compile(r'^[01]+$')
    return bool(binary_pattern.match(value))


def getLength() -> int:
    while True:
        try:
            result = int(input(lengthMenuText))
            if result == 0:
                break
            if result not in range(1, 33):
                print("Only between 0 - 32 bits")
                continue
            return result
        except:
            print("!!! Only integer values!")


def insertBinary():
    while True:
        try:
            binaryNumber = str(int(input(enterBinaryText)))
            for char in binaryNumber():
                if char not in ["1", "0"]:
                    print("Incorrect binary number!")
                    continue
            if binaryNumber:
                return binaryNumber
            else:
                print("Incorrect binary number!")
        except:
            print("Only binary values!")


def randomBinary(length) -> str:
    return "".join([choice("01") for _ in range(length)])


def getBinary():
    choices = ("1", "2", "0")
    while True:
        choice = input(getBinaryText)
        if choice not in choices:
            print("Only given choices")
            continue
        if choice == "0":
            break
        if choice == "1":
            return insertBinary()
        if choice == "2":
            length = getLength()
            result = randomBinary(length)
            print(f"Binary: {result}")
            return result
