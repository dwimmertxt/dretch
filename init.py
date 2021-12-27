import curses

def config_curses(stdscr):
	curses.noecho()
	curses.cbreak()
	curses.start_color()
	curses.use_default_colors()
	[curses.init_pair(i, i, -1) for i in range(0, 255)]

def init_state():
	state = {}
	state["window"] = 1
	state["drawing"] = {
		"curs_pos": {'y': 1, 'x': 1}
		}
	state["palette"] = {
		"range": [i for i in range(-1, 16) if i != 0],
		"current": {'y': 1, 'x': 2, 'column_select': 1, 'colour': 1}
		}
	return state

def init_win_info():
	win_info = curses.newwin(1, 80, 0, 0)
	win_info.keypad(True)
	win_info.nodelay(True)
	win_info.addstr(0, 0, 'dretch v0.0.1')
	
	win_info.refresh()
	return win_info

def init_win_palette(palette):
	win_palette = curses.newwin(10, 5, 1, 0)
	win_palette.keypad(True)
	win_palette.nodelay(True)
	win_palette.border(0, 0, 0, 0, 0, 0, 0, 0)

	for colour,i in enumerate(palette["range"]):
		win_palette.addstr(
			(i%8)+1, 1 if i < 8 else 3, 
			'\u2588', curses.color_pair(colour)
			)

	win_palette.refresh()
	return win_palette

def init_win_drawing():
	win_drawing = curses.newwin(10, 75, 1, 5)
	win_drawing.keypad(True)
	win_drawing.nodelay(True)
	win_drawing.border(0, 0, 0, 0, 0, 0, 0, 0)

	win_drawing.refresh()
	return win_drawing