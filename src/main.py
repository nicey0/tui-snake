from state import State
from snake import run_game


if __name__ == '__main__':
    states: dict = {
        "game": run_game
    }
    state = State("game", states, True)
    state.run()
