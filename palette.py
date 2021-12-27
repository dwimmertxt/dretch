import curses

def update_palette(win_palette, state):
	curses.curs_set(0)
	while True:
		user_input = win_palette.getch()
		if user_input == 9:
			state["window"] = 1
			return state
		if user_input in range(258, 262):
			state["palette"]["current"] = select_colour(
				win_palette,
				state["palette"]["current"], 
				user_input
				)

def select_colour(win_palette, current, user_input):
	win_palette.addch(current['y'], current['x'], ' ')

	if user_input == 259 and current['y'] > 1:
		current['y'] -= 1
	elif user_input == 258 and current['y'] < 8:
		current['y'] += 1
	elif user_input == 260:
		current['column_select'] = 0
	elif user_input == 261:
		current['column_select'] = 1
	
	current['colour'] = current['y']-1 if current['column_select'] == 0 else current['y']+7

	win_palette.addstr(
		current['y'], current['x'],
		'<' if current['column_select'] == 0 else '>', 
		curses.color_pair(current['colour'])
		)
	win_palette.refresh()
	
	return current