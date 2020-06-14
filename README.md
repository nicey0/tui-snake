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
- [ ] End
    - [ ] \<score\>
    - [ ] Play again
    - [ ] Quit to Main Menu
- [ ] Menu
    - [ ] Start
    - [ ] Quit
### Input
- [X] Running
    - [X] j goes left
    - [X] k goes right
    - [ ] Q quits to main menu
- [ ] End
    - [ ] j moves up - X
    - [ ] k moves down - X
    - [ ] \<CR\> enters selected option
    - [ ] r plays again
    - [ ] q quits to main menu
- [ ] Menu
    - [ ] j moves up - X
    - [ ] k moves down - X
    - [ ] q quits game - X
    - [ ] \<CR\> enters selected option - X
### Score
- [X] Add score system (apples eaten)
