import curses


def process_key(key: int, cursor: int, menu_items: list) -> (int, str):
    game_state = ""
    if key == ord('j'):  # go down
        cursor += 1 if cursor < len(menu_items)-1 else \
            -cursor
    elif key == ord('k'):  # go up
        cursor -= 1 if cursor > 0 else \
            -(len(menu_items)-1)
    elif key == ord('q'):  # exit
        pass
    elif key == curses.KEY_ENTER or key == ord('\n') or key == 13:
        game_state = select(cursor, menu_items)
    return (cursor, game_state)


def select(option: int, menu_items: list) -> str:
    s: str = menu_items[option].lower()
    if s.find('start') != -1:
        return "game"
    elif s.find('exit') != -1 or s.find('quit') != -1:
        return " EXIT "
    return ""


def run_mainmenu(scr: curses.window):
    curses.curs_set(0)
    title: str = "Snake"
    menu_items: list = ["Start", "Exit"]
    game_state = ""
    cursor: int = 0
    while True:
        scr.erase()
        scr.addstr(1, 1, title, curses.A_BOLD)
        scr.addstr(2, 1, '-'*(len(title)*2))
        for i, item in enumerate(menu_items):
            if i == cursor:
                scr.addstr(3+i, 2, item, curses.A_REVERSE)
            else:
                scr.addstr(3+i, 2, item)
        # ++ Tick ++
        key = scr.getch()
        cursor, game_state = process_key(key, cursor, menu_items)
        if game_state != "":
            return game_state
        # -- Tick --
        scr.refresh()
