import curses


snake: list = [(0, 0)]  # head is [0], body is [1:]. the snake
for x in range(1, 11):
    snake.append((0, x))


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
