import curses


NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)


def tick(snake: list, direction: tuple, key: int, apples: list, score: int,
         minx: int, maxc: tuple) -> (list, tuple, list, int):
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
    # Apples
    for apple in apples:
        if snake[0] == apple:
            snake = big_snek(snake)
            apples.remove(apple)
            score += 1
    return (snake, direction, apples, score)


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


def main(scr: curses.window):
    curses.curs_set(0)
    scr.nodelay(True)
    status_w: int = 2
    snake: list = [(0, status_w+1), (0, status_w+2), (0, status_w+3)]
    for i in range(4, 30+1):
        snake.append((0, status_w+i))
    direction = WEST
    apples: list = [(5, 5), (8, 8)]
    score = 0
    while True:
        scr.clear()
        draw_snek(scr, snake)
        draw_apples(scr, apples)
        scr.addstr(0, 0, str(score))
        snake, direction, apples, score = tick(snake, direction, scr.getch(),
                                               apples, score, status_w,
                                               scr.getmaxyx())
        scr.refresh()
        curses.napms(100)


if __name__ == '__main__':
    curses.wrapper(main)
