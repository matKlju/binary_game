from menu.menuTexts import gameDifficultyText, gameMenu
from conversion.binary import randomBinary
from conversion.decimal import insertDecimal


def gameDifficulty():
    while True:
        choice = int(input(gameDifficultyText))
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
    while True:
        choice = int(input(gameMenu))
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

