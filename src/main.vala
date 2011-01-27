/**
 * main.vala
 * The Shittiest Game Ever: Adventure
 * Copyright (C) 2011-2012  Alexandre Gauthier
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 */

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

