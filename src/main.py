import curses


NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)

snake: list = [(0, 0)]  # head is [0], body is [1:]. the snake
for x in range(1, 11):
    snake.append((0, x))


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


def main(scr: curses.window):
    curses.curs_set(0)
    # is made of (y, x) pairs.
    for y, x in snake[1:]:
        scr.addstr(y, x, '@')
    scr.addstr(snake[0][0], snake[0][1], '#')
    scr.refresh()
    scr.getch()


if __name__ == '__main__':
    curses.wrapper(main)
