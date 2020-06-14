import curses


NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)


def process_key(key: int, direction: tuple) -> tuple:
    # Key processing
    if key == ord('j'):
        direction = go_left(direction)
    elif key == ord('k'):
        direction = go_right(direction)
    return direction


def move_snake(snake: list, direction: tuple) -> list:
    # Movement
    for i in range(1, len(snake))[::-1]:
        snake[i] = snake[i-1]
    snake[0] = (snake[0][0] + direction[0],
                snake[0][1] + direction[1])
    return snake


def portals(snake: list, minx: int, maxc: tuple) -> list:
    # y
    if snake[0][0] < 0:
        snake[0] = (maxc[0]-1, snake[0][1])
    elif snake[0][0] >= maxc[0]:
        snake[0] = (0, snake[0][1])
    # x
    if snake[0][1] < minx:
        snake[0] = (snake[0][0], maxc[1]-1)
    elif snake[0][1] >= maxc[1]:
        snake[0] = (snake[0][0], minx)
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


def draw_statusbar(scr: curses.window, status_w: int, score: int):
    def section(word: str, status_w: int):
        word = "--"+word
        return word + "-"*(status_w-len(word)+1)
    for line in range(scr.getmaxyx()[0]):
        scr.addstr(line, status_w + 1, "|")
    scr.addstr(1, 0, section("SCORE", status_w))
    scr.addstr(2, 1, str(score))
    # Help menu
    help_menu = ["j: turn left", "k: turn right", "q: quit to main menu"]
    starty = scr.getmaxyx()[0]-1-len(help_menu)-1
    scr.addstr(starty, 0, section("HELP", status_w))
    for i, item in enumerate(help_menu):
        if len(item) >= status_w:
            item = item[:-2] + "-"
        scr.addstr(starty + i + 1, 1, item)


def main(scr: curses.window):
    curses.curs_set(0)
    scr.nodelay(True)
    status_w: int = 25

    midy = int(scr.getmaxyx()[0] / 2)
    midx = int(scr.getmaxyx()[1] / 2)
    snake: list = [(midy, status_w+midx), (midy, status_w+midx+1),
                   (midy, status_w+midx+2)]
    direction = WEST
    apples: list = []
    score = 0
    while True:
        scr.erase()
        draw_statusbar(scr, status_w, score)
        draw_snek(scr, snake)
        draw_apples(scr, apples)
        # ++ Tick ++
        key = scr.getch()
        direction = process_key(key, direction)
        snake = move_snake(snake, direction)
        snake = portals(snake, status_w+2, scr.getmaxyx())
        snake, apples, nscore = eat_apples(snake, apples)
        score += nscore
        # -- Tick --
        scr.refresh()
        curses.napms(60)


if __name__ == '__main__':
    curses.wrapper(main)
