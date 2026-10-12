import curses
from curses import wrapper

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # Print a message
    stdscr.addstr(10, 45, "Teste daqui")

    # Refresh the screen to show the message
    stdscr.refresh()

    # Wait for user input
    stdscr.getch()

wrapper(main)