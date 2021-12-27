#!/usr/bin/env python
"""A simple TUI to draw/edit text art for *fetch utils."""

import curses
import init as i
import palette as p
import draw as d

__author__ = "dwimmer"
__copyright__ = "dwimmer"
__credits__ = "dwimmer"

__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "dwimmer"
__email__ = "dwimmer.tm@pm.me"
__status__ = "Prototype"

def main():
	'''
		Automates curses housekeeping - thankfully.
	'''
	curses.wrapper(curses_main)

def curses_main(stdscr):
	i.config_curses(stdscr)
	state = i.init_state()
	win_info = i.init_win_info()
	win_palette = i.init_win_palette(state["palette"])
	win_drawing = i.init_win_drawing()

	while True:
		if state["window"] == 0:
			state = p.update_palette(win_palette, state)
		elif state["window"] == 1:
			state = d.update_drawing(win_drawing, state)


main()

