from state import State
from snake import run_game
from mainmenu import run_mainmenu
from end import run_end


if __name__ == '__main__':
    states: dict = {
        "game": run_game,
        "mainmenu": run_mainmenu,
        "end": run_end
    }
    state = State("mainmenu", states, True)
    args = []
    results = 0
    while state.running:
        if state == "end":
            args = [results]
        else:
            args = []
        next_state, results = state.run(*args)
        if next_state == " EXIT ":
            break
        state.switch(next_state)
