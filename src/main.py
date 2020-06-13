import curses


NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)


def tick(snake: list, direction: tuple, key: int, apples: list,
         maxc: tuple) -> (list, tuple):
    # Key processing
    if key == ord('j'):
        direction = go_left(direction)
    elif key == ord('k'):
        direction = go_right(direction)
    # Movement
    for i in range(1, len(snake))[::-1]:
        snake[i] = snake[i-1]
    snake[0] = (snake[0][0] + direction[0],
                snake[0][1] + direction[1])
    # Portals
    if snake[0][0] < 0:
        snake[0] = (maxc[0]-1, snake[0][1])
    elif snake[0][0] >= maxc[0]:
        snake[0] = (0, snake[0][1])
    if snake[0][1] < 0:
        snake[0] = (snake[0][0], maxc[1]-1)
    elif snake[0][1] >= maxc[1]:
        snake[0] = (snake[0][0], 0)
    # Apples
    for apple in apples:
        if snake[0] == apple:
            snake = big_snek(snake)
    return (snake, direction)


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


def main(scr: curses.window):
    curses.curs_set(0)
    scr.nodelay(True)
    snake: list = [(0, 2), (0, 1), (0, 0)]  # head is [0], body is [1:].
    direction = EAST
    while True:
        scr.clear()
        draw_snek(scr, snake)
        snake, direction = tick(snake, direction, scr.getch(), scr.getmaxyx())
        scr.refresh()
        curses.napms(100)


if __name__ == '__main__':
    curses.wrapper(main)
