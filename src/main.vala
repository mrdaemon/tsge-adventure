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


class TsgeMain : Object {

	/**
	 * Program entry point
	 */
	public static int main(string[] args) {

		init_display();

		/* Create a window
		 * height/lines, width/columns, y, x) */
		var console = new Window(LINES - 4, COLS - 8, 2, 4);

		console.bkgdset (COLOR_PAIR(1) | Attribute.BOLD);
		console.addstr("Loading...");
		console.clrtobot(); // clear to bottom, doesn't move cursor
		console.getch(); // Read char

		cleanup();

		return 0;
	}

	/**
	 * Initalize curses display
	 */
	private static void init_display(){
		// Init curses screen
		initscr();

		// Color Support Check
		if(has_colors()) {
			start_color();
			init_pair(1, Color.YELLOW, Color.BLUE); // Default shell color
		} else {
			stderr.printf("ERROR: Your terminal does not support " +
				"color mode. Aborting...\n");
			Process.exit(1);
		}

		raw();
		noecho();
		stdscr.keypad(true);

	}

	/**
	 * Cleanup and reset terminal
	 */
	private static void cleanup(){
		// Reset terminal mode
		endwin();
		stdout.printf("So long and thanks for all the shoes.\n");
	}
}
