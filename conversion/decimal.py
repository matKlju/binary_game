from random import randint
from menu.menuTexts import maxValueText, insertDecimalText, getDecimalText


def maxValue() -> int:
    while True:
        try:
            return int(input(maxValueText))
        except:
            print("!!! Only integer values!")


def insertDecimal():
    while True:
        try:
            return int(input(insertDecimalText))
        except:
            print("!!! Only integer values!")


def randomDecimal() -> str:
    length = maxValue()
    return randint(1, length)


def getDecimal():
    choices = ("1", "2", "0")
    while True:
        choice = input(getDecimalText)
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
