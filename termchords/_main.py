import curses
import sys


BLACK_KEY = curses.COLOR_BLACK, curses.COLOR_WHITE
WHITE_KEY = curses.COLOR_WHITE, curses.COLOR_BLACK


class Colors:
    RegularText = 1
    UserInput = 2
    BlackKey = 3
    WhiteKey = 4


def main_window(stdscr):
    k = 0
    cursor_x = 0
    cursor_y = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()

    curses.init_pair(Colors.RegularText, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(Colors.UserInput, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(Colors.BlackKey, BLACK_KEY[0], BLACK_KEY[1])
    curses.init_pair(Colors.WhiteKey, WHITE_KEY[0], WHITE_KEY[1])

    # Loop where k is the last character pressed
    while k != ord("q"):

        # Initialization
        stdscr.clear()
        # height, width = stdscr.getmaxyx()
        draw_octave(stdscr, 2, 0, first=True, last=False)

        stdscr.move(0, 0)

        stdscr.addstr(0, 0, "Enter chord: ", curses.color_pair(Colors.RegularText))
        stdscr.attron(curses.color_pair(Colors.UserInput))

        curses.echo()
        input = stdscr.getstr(0, 13, 20)
        curses.noecho()
        stdscr.move(0, 0)
        stdscr.attron(curses.color_pair(Colors.RegularText))

        #  # Render status bar
        #  stdscr.attron(curses.color_pair(3))

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()


def draw_octave(stdscr, r: int, c: int, first: bool, last: bool) -> None:
    height, width = stdscr.getmaxyx()
    # ┌─┬─┐
    # │ │ │
    # ├─┼─┤
    # │ │ │
    # └─┴─┘
    oct_width = 36
    if first:
        stdscr.addstr(r + 0, c, "┌")
        stdscr.addstr(r + 1, c, "│")
        stdscr.addstr(r + 2, c, "│")
        stdscr.addstr(r + 3, c, "│")
        stdscr.addstr(r + 4, c, "│")
        stdscr.addstr(r + 5, c, "└")
    else:
        stdscr.addstr(r + 0, c, "┬")
        stdscr.addstr(r + 1, c, "│")
        stdscr.addstr(r + 2, c, "│")
        stdscr.addstr(r + 3, c, "│")
        stdscr.addstr(r + 4, c, "│")
        stdscr.addstr(r + 5, c, "┴")

    last_c = oct_width
    if last:
        stdscr.addstr(r + 0, last_c, "┐")
        stdscr.addstr(r + 1, last_c, "│")
        stdscr.addstr(r + 2, last_c, "│")
        stdscr.addstr(r + 3, last_c, "│")
        stdscr.addstr(r + 4, last_c, "│")
        stdscr.addstr(r + 5, last_c, "┘")
    else:
        stdscr.addstr(r + 0, last_c, "┬")
        stdscr.addstr(r + 1, last_c, "│")
        stdscr.addstr(r + 2, last_c, "│")
        stdscr.addstr(r + 3, last_c, "│")
        stdscr.addstr(r + 4, last_c, "│")
        stdscr.addstr(r + 5, last_c, "┴")

    stdscr.addstr(r + 0, c + 1, "──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬")
    stdscr.addstr(r + 1, c + 1, "  │  │  │  │  │  │  │  │  │  │  │  │")
    stdscr.addstr(r + 2, c + 1, "  │  │  │  │  │  │  │  │  │  │  │  │")
    stdscr.addstr(r + 3, c + 1, "  └┬─┘  └┬─┘  └┬─┘  │  └┬─┘  └┬─┘  │")
    stdscr.addstr(r + 4, c + 1, "   │     │     │    │   │     │    │")
    stdscr.addstr(r + 5, c + 1, "───┴─────┴─────┴────┴───┴─────┴────┴")


def main():
    curses.wrapper(main_window)
    sys.exit(0)


if __name__ == "__main__":
    main()
