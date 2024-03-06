from random import randint


def maxValue() -> int:
    text = """
Max random number 
--------------------------
Max: """
    while True:
        try:
            return int(input(text))
        except:
            print("!!! Only integer values!")


def insertDecimal():
    text = """
Enter decimal number
--------------------------
Decimal: """
    while True:
        try:
            return int(input(text))
        except:
            print("!!! Only integer values!")


def randomDecimal() -> str:
    length = maxValue()
    return randint(1, length)


def getDecimal():
    text = """
DEC -> BIN
0. EXIT - return
1. Insert decimal
2. Generate decimal
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
            return insertDecimal()
        if choice == "2":
            result = randomDecimal()
            print(f"Decimal: {result}")
            return result
