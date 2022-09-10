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
        self.rows = []
        self.finished = False
        for idx in range(5):
            bt = Button(random.randint(1, 8))
            while bt in self.target:
                bt = Button(random.randint(1, 8))
            self.target.append(bt)

    def show_buttons(self, buttons, idx=None, show_score=True):
        b0 = buttons[0].name
        b1 = buttons[1].name
        b2 = buttons[2].name
        b3 = buttons[3].name
        b4 = buttons[4].name
        blst = []
        wlst = []
        for n in range(5):
            bt = buttons[n]
            if bt == self.target[n]:
                blst.append('x')
            elif bt in self.target:
                wlst.append('o')
        score = blst + wlst
        while len(score) < 5:
            score.append('_')
        if show_score:
            print(f"{idx:2} | {b0:6} | {b1:6} | {b2:6} | {b3:6} | {b4:6} | {score}")
        else:
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
            print(f"Error: invalid: {[x.name for x in btnres]}")
            return None

        return btnres


def main():
    print("Hello Mastermind")

    board = Board()
    # board.show_buttons(board.target, show_score=False)

    while not board.finished:
        try:
            buttons = board.read_input()
            if not buttons:
                continue
        except KeyboardInterrupt:
            return

        # No duplicaes, excatly 5
        board.rows.append(buttons)

        for idx in range(len(board.rows)):
            row = board.rows[idx]
            board.show_buttons(row, idx+1)

        success = buttons == board.target
        if success:
            print("Mastermind, you won!🥳")
            board.finished = True

        if len(board.rows) >= 12:
            print("Game over!👾")
            board.finished = True


if __name__ == "__main__":
    main()
