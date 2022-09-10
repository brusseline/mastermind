import random

from enum import IntEnum


class Button(IntEnum):
    Red = 1,
    Orange = 2,
    Yellow = 3,
    Green = 4,
    Blue = 5,
    Black = 6,
    Brown = 7,
    White = 8


class Board:

    def __init__(self):
        self.target = []
        self.finished = False
        for idx in range(5):
            bt = Button(random.randint(1, 8))
            while bt in self.target:
                bt = Button(random.randint(1, 8))
            self.target.append(bt)

    def show_buttons(self, blst):
        b0 = blst[0].name
        b1 = blst[1].name
        b2 = blst[2].name
        b3 = blst[3].name
        b4 = blst[4].name
        print(f"| {b0:6} | {b1:6} | {b2:6} | {b3:6} | {b4:6} |")

    def read_input(self):
        '''
            Read user input and return list of buttons
            - no duplicates
            - exactly 5
        '''

        # Read comma separated list of string
        print("your turn: ", end='')
        usrlst = input().split(' ')

        if len(usrlst) < 5:
            print(f"Error: length is too short: {usrlst}")
            return None

        if len(usrlst) > 5:
            print(f"Error: length is too long: {usrlst}")
            return None

        btnres = []
        for ch in usrlst:
            chup = ch.upper()
            btnlst = [bt for bt in Button if bt.name.upper().startswith(chup)]
            if len(btnlst) < 1:
                print(f"Error: cannot map: {ch} ")
            elif len(btnlst) > 1:
                print(f"Error: ambiguous: {ch} => {btnlst}")
            elif btnlst[0] in btnres:
                print(f"Error: duplicate: {ch} => {btnres}")
            else:
                btnres.append(btnlst[0])
        if len(btnres) != 5:
            print(f"Error: invalid: {btnres}")
            return None

        return btnres


def main():
    print("Hello Mastermind")

    board = Board()
    board.show_buttons(board.target)
    while not board.finished:
        try:
            buttons = board.read_input()
            if not buttons:
                continue
        except KeyboardInterrupt:
            return

        # No duplicaes, excatly 5
        board.show_buttons(buttons)
        success = buttons == board.target

        if success:
            print("Mastermind, you won 🥳")
            board.finished = True
        else:
            print("Try again, maybe next time 😭")


if __name__ == "__main__":
    main()
