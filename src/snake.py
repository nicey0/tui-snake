import curses
from random import randint


NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)
MAX_APPLES = 5


def process_key(key: int, direction: tuple) -> (tuple, str):
    game_state = ""
    if key == ord('j'):
        direction = go_left(direction)
    elif key == ord('k'):
        direction = go_right(direction)
    elif key == ord('Q'):
        game_state = "mainmenu"
    return (direction, game_state)


def move_snake(snake: list, direction: tuple) -> list:
    # Movement
    for i in range(1, len(snake))[::-1]:
        snake[i] = snake[i-1]
    snake[0] = (snake[0][0] + direction[0],
                snake[0][1] + direction[1])
    return snake


def check_loss(snake) -> bool:
    return snake[0] in snake[1:]


def portals(snake: list, direction: tuple, minx: int, maxc: tuple) -> list:
    nexty: int = snake[0][0]
    nextx: int = snake[0][1]
    # y
    if snake[0][0] < 0:
        nexty = maxc[0]-1
    elif snake[0][0] >= maxc[0]:
        nexty = 0
    # x
    if snake[0][1] < minx:
        nextx = maxc[1]-1
    elif snake[0][1] >= maxc[1]:
        nextx = minx
    snake[0] = (nexty, nextx)
    return snake


def eat_apples(snake: list, apples: list) -> (list, list, int):
    score = 0
    # Apples
    for apple in apples:
        if snake[0] == apple:
            snake = big_snek(snake)
            apples.remove(apple)
            score += 1
    return (snake, apples, score)


def go_left(direction: tuple) -> tuple:
    if direction == NORTH:
        return WEST
    elif direction == SOUTH:
        return EAST
    elif direction == EAST:
        return NORTH
    elif direction == WEST:
        return SOUTH


def go_right(direction: tuple) -> tuple:
    if direction == NORTH:
        return EAST
    elif direction == SOUTH:
        return WEST
    elif direction == EAST:
        return SOUTH
    elif direction == WEST:
        return NORTH


def big_snek(snake: list) -> list:
    return snake + [snake[-1]]


def draw_snek(scr: curses.window, snake: list):
    for y, x in snake[1:]:
        scr.addstr(y, x, '@')
    scr.addstr(snake[0][0], snake[0][1], '#')


def draw_apples(scr: curses.window, apples: list):
    for y, x in apples:
        scr.addstr(y, x, '$')


def draw_statusbar(scr: curses.window, maxc: tuple, status_w: int, score: int):
    def section(word: str, status_w: int):
        word = "--"+word
        return word + "-"*(status_w-len(word)+1)
    for line in range(maxc[0]):
        scr.addstr(line, status_w + 1, "|")
    scr.addstr(maxc[0], status_w + 1, "+")
    scr.addstr(maxc[0], 0, "-"*maxc[1])
    scr.addstr(maxc[0], status_w + 1, "+")
    scr.addstr(1, 0, section("SCORE", status_w))
    scr.addstr(2, 1, str(score))
    # Help menu
    help_menu = ["#: snake head", "@: snake body", "$: apple", "j: turn left",
                 "k: turn right", "q: quit to main menu"]
    starty = maxc[0]-1-len(help_menu)-1
    scr.addstr(starty, 0, section("HELP", status_w))
    for i, item in enumerate(help_menu):
        if len(item) >= status_w:
            item = item[:-2] + "-"
        scr.addstr(starty + i + 1, 1, item)


def create_apples(snake: list, apples: list, amount: int, minx: int,
                  maxc: tuple) -> list:
    while amount > 0:
        y = randint(0, maxc[0]-1)
        x = randint(minx, maxc[1]-1)
        if (y, x) not in apples and (y, x) not in snake:
            apples.append((y, x))
            amount -= 1
    return apples


def run_game(scr: curses.window):
    curses.curs_set(0)
    scr.nodelay(True)
    game_state = ""
    status_w: int = 25
    maxy = scr.getmaxyx()[0]-1
    maxx = scr.getmaxyx()[1]

    midy = int(maxy / 2)
    midx = int(maxx / 2)
    snake: list = [(midy, status_w+midx), (midy, status_w+midx+1)]
    direction = WEST
    apples: list = []
    score = 0
    while True:
        scr.erase()
        draw_statusbar(scr, (maxy-1, maxx), status_w, score)
        draw_snek(scr, snake)
        draw_apples(scr, apples)
        # ++ Tick ++
        key = scr.getch()
        direction, game_state = process_key(key, direction)
        snake = move_snake(snake, direction)
        snake = portals(snake, direction, status_w+2, (maxy-1, maxx))
        snake, apples, nscore = eat_apples(snake, apples)
        apples = create_apples(snake, apples, MAX_APPLES - len(apples),
                               status_w, (maxy, maxx))
        score += nscore
        if game_state != "":
            return game_state
        # -- Tick --
        scr.refresh()
        if check_loss(snake):
            curses.napms(1000)
            return "end"
        curses.napms(60)
