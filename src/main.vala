using Curses;

int main(string[] args) {
	initscr();

	start_color();
	init_pair(1, Color.YELLOW, Color.BLUE);

	/* Create a window
	 * height/lines, width/columns, y, x) */
	var win = new Window(LINES - 4, COLS - 8, 2, 4);

	win.bkgdset (COLOR_PAIR(1) | Attribute.BOLD);
	win.addstr("Sup, fuckers");
	win.clrtobot(); // clear to bottom, doesn't move cursor
	win.getch(); // Read char

	endwin(); // Reset terminal mode

	return 0;
}

