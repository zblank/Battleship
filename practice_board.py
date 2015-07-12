from blessings import Terminal

t = Terminal()

final_list = []
for num in range(9):
	l = []
	for num in range(10):
		l.append('O')
	final_list.append(l)
last_line = []
for num in range(10):
	last_line.append("M")
final_list.append(last_line)

print(t.move(-30,1)+"hey")
print("Hello")

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
			if x == "M":
				new_row += "    {t.blue}" + x
			elif x == "O":
				new_row += "    {t.normal}" + x
			elif x == "X":
				new_row += "    {t.red}" + x
			else:
				new_row += "    {t.green}" + x
		print(new_row.format(t=t))
		print("")
		xaxis2 += "    {t.normal}" + str(key)
		xaxis1 += "    {t.normal}"  + "-"
	print(xaxis1.format(t=t))
	print(xaxis2.format(t=t))


# display_users_board(final_list)
#display_own_board(final_list)

