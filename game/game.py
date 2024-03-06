from conversion.binary import randomBinary
from conversion.decimal import insertDecimal


def gameDifficulty():
    text = """
0. EXIT - return
1. Easy        4 bit  1 nibble (1/2 byte)15 dec max
3. Medium      8 bit  1 byte            256 dec max
5. Hard       16 bit  2 byte         65 535 dec max
7. Very hard  32 bit  4 byte  4 294 967 295 dec max
--------------------------
"""
    while True:
        choice = int(input(text))
        if choice not in range(8):
            print("!!! Only given choices")
            continue
        if choice == 0:
            break
        return choice


def guessBinary(difficulty):
    binaryNumber = int(randomBinary(difficulty))
    decimalGuess = insertDecimal()
    if binaryNumber == decimalGuess:
        return "Correct!"
    return "False!"


def guessDecimal(difficulty):
    pass


def game():
    text = """
0. EXIT - return
1. Guess binary
2. Guess decimal
--------------------------
"""
    while True:
        choice = int(input(text))
        if choice not in range(3):
            print("!!! Only given choices")
            continue
        difficulty = gameDifficulty()
        if choice == 0:
            break
        if choice == 1:
            result = guessBinary(difficulty)
            print(result)
        if choice == 2:
            result = guessDecimal(difficulty)

