final_list = []
for num in range(10):
	l = []
	for num in range(10):
		l.append('O')
	final_list.append(l)


def display_own_board(board):
	for x in board:
		print(x)
	print("")

def display_own_board(board):
	for row in board:
		new_row = ''
		for x in row:
			new_row += " " + x
		print(new_row)


def display_users_board(board):
	xaxis1 = "  "
	xaxis2 = "  "
	for key, value in enumerate(board):
		new_row = str(key) + "|"
		for x in value:
			new_row += "    " + x
		print(new_row)
		print("")
		xaxis2 += "    " + str(key)
		xaxis1 += "    "  + "-"
	print(xaxis1)
	print(xaxis2)


display_users_board(final_list)
#display_own_board(final_list)