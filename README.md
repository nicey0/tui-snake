# tui-snake
Simple Snake clone for Unix terminals, written in Python+Curses

---

## Todo
### Curses display
### Snake
- [X] Movement
- [X] Apple eating
- [X] Wrapping (teleport down if y < 0 and etc)
### Apples
- [X] Disappear when eaten
- [X] Create new apples after the last was eaten
- [X] Don't spawn apples on top of the snake
### Game state
- [X] Running
    - [X] Fullscreen area
    - [X] 20-width area to the left (score, apples onscreen, etc)
- [X] End
    - [X] \<score\>
    - [X] Play again
    - [X] Quit to Main Menu
- [X] Menu
    - [X] Start
    - [X] Quit
### Input
- [X] Menu
    - [X] j moves up - X
    - [X] k moves down - X
    - [X] q quits game - X
    - [X] \<CR\> enters selected option - X
- [X] Running
    - [X] j goes left
    - [X] k goes right
    - [X] Q quits to main menu
- [X] End
    - [X] j moves up - X
    - [X] k moves down - X
    - [X] \<CR\> enters selected option
    - [X] q quits to main menu
### Score
- [X] Add score system (apples eaten)
