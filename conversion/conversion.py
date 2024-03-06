from .binary import getBinary
from .decimal import getDecimal


def conversion():
    text = """
0. EXIT
1. Binary to decimal
2. Decimal to binary
--------------------------
"""
    choices = ("1", "2", "0")
    while True:
        choice = input(text)
        if choice not in choices:
            print("!!! Only given choices")
            continue
        if choice == "0":
            break
        if choice == "1":
            result = convertBinary()
            print(f"Decimal: {result}")
        if choice  == "2":
            result = convertDecimal()
            print(f"Binary: {result}")


def convertBinary() -> int:
    binary = getBinary()
    return int(binary, 2)


def convertDecimal() -> str:
    decimalNumber = getDecimal()
    return bin(decimalNumber)[2:]
