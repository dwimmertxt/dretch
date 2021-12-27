import curses

def update_drawing(win_drawing, state):
	curses.curs_set(1)
	while True:
		user_input = win_drawing.getch()
		win_drawing.move(
			state["drawing"]['curs_pos']['y'], 
			state["drawing"]['curs_pos']['x']
			)
		if user_input == 9:
			state["window"] = 0
			return state
		elif user_input in range(258, 262):
			state["drawing"]['curs_pos'] = move_cursor(
				win_drawing,
				state["drawing"]['curs_pos'], 
				user_input
				)
		elif user_input != -1 and user_input != 9:
			place_chr(win_drawing, state, user_input)

def move_cursor(win_drawing, curs_pos, user_input):
	if user_input == 259 and curs_pos['y'] > 1:
		curs_pos['y'] -= 1
	elif user_input == 258 and curs_pos['y'] < 8:
		curs_pos['y'] += 1
	elif user_input == 260 and curs_pos['x'] > 1:
		curs_pos['x'] -= 1
	elif user_input == 261 and curs_pos['x'] < 73:
		curs_pos['x'] += 1 
	win_drawing.move(curs_pos['y'], curs_pos['x'])
	win_drawing.refresh()
	return curs_pos

def place_chr(win_drawing, state, user_input):
	win_drawing.addstr(
		chr(user_input), 
		curses.color_pair(state["palette"]["current"]["colour"]))
	if state["drawing"]["curs_pos"]["x"] != 73:
		state["drawing"]["curs_pos"]["x"] += 1
		win_drawing.move(
			state["drawing"]["curs_pos"]["y"],
			state["drawing"]["curs_pos"]["x"]
			)
	return state
