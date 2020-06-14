from state import State
from snake import run_game
from mainmenu import run_mainmenu


if __name__ == '__main__':
    states: dict = {
        "game": run_game,
        "mainmenu": run_mainmenu
    }
    state = State("mainmenu", states, True)
    while state.running:
        next_state = state.run()
        if next_state == " EXIT ":
            break
        state.switch(next_state)
