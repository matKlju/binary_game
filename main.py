import sys
from game.game import game
from conversion.conversion import conversion


def mainMenu():
    text = """
0. EXIT - return
1. Conversion
2. Game
3. Info
--------------------------
"""
    choices = ("1", "2", "3", "0")
    while True:
        choice = input(text)
        if choice not in choices:
            print("!!! Only given choices")
            continue
        if choice == "0":
            print("Bye!")
            sys.exit()
        if choice == "1":
            conversion()
        if choice  == "2":
            game()
        # if choice  == "3":
        #     info()

def main():
    mainMenu()


if __name__ == "__main__":
    main()
