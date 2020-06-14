import curses
from snake import run_game


if __name__ == '__main__':
    state = "game"
    if state == "mainmenu":
        pass
    elif state == "game":
        curses.wrapper(run_game)
    elif state == "end":
        pass
