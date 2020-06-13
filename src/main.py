import curses


NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)

snake: list = [(0, 0)]  # head is [0], body is [1:]. the snake
direction = EAST


def tick(snake: list, direction: tuple, key: int) -> (list, tuple):
    if key == ord('j'):
        direction = go_left(direction)
    elif key == ord('k'):
        direction = go_right(direction)
    for i in range(1, len(snake))[::-1]:
        snake[i] = snake[i-1]
    snake[0] = (snake[0][0] + direction[0],
                snake[0][1] + direction[1])


def go_left(direction: tuple) -> tuple:
    if direction == NORTH:
        return EAST
    elif direction == SOUTH:
        return WEST
    elif direction == EAST:
        return NORTH
    elif direction == WEST:
        return SOUTH


def go_right(direction: tuple) -> tuple:
    if direction == NORTH:
        return WEST
    elif direction == SOUTH:
        return EAST
    elif direction == EAST:
        return SOUTH
    elif direction == WEST:
        return NORTH


def draw_snek(scr: curses.window, snake: list):
    for y, x in snake[1:]:
        scr.addstr(y, x, '@')
    scr.addstr(snake[0][0], snake[0][1], '#')


def main(scr: curses.window):
    curses.curs_set(0)
    scr.nodelay(True)
    while True:
        draw_snek(scr, snake)
        tick(snake, direction, scr.getch())
        scr.refresh()


if __name__ == '__main__':
    curses.wrapper(main)
