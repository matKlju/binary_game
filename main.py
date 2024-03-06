import sys
from game.game import game
from menu.menuTexts import mainMenuText
from conversion.conversion import conversion


def mainMenu():
    choices = ("1", "2", "3", "0")
    while True:
        choice = input(mainMenuText)
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
