import curses
from typing import Callable


class State:
    running: bool
    _states: dict
    _game_state: Callable

    def __init__(self, start: str, states: dict, running: bool = False):
        self._game_state = states[start]
        self._states = states
        self.running = running

    def switch(self, game_state) -> bool:
        if game_state in self.states:
            self._game_state = self.states[game_state]
            return True
        return False

    def run(self):
        curses.wrapper(self._game_state)

    def __eq__(self, game_state: str):
        return self._game_state == self._states[game_state]
