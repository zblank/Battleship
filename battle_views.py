import os
# You guys will have to install the blessings library
# if you don't already have it
# Documentation here -> https://github.com/erikrose/blessings

from blessings import Terminal

t = Terminal()

class Views:
	def __init__(self):
		pass

	def display_own_board(self,board):
		xaxis = "   "
		for key, value in enumerate(board):
			new_row = "{t.normal}  " + str(key)
			for x in value:
				if x[1] == "M":
					new_row += "{t.normal}  |  {t.bold_blue}" + x[1]
				elif x[1] == "O":
					new_row += "{t.normal}  |  {t.normal}" + " "
				elif x[1] == "X":
					new_row += "{t.normal}  |  {t.bold_red}" + x[1]
				else:
					new_row += "{t.normal}  |  {t.bold_green}" + x[1]
			new_row += "{t.normal}  |"
			print(new_row.format(t=t))
			print("{t.normal}     -------------------------------------------------------------".format(t=t))
			xaxis += "     {t.normal}" + str(key)
		print(xaxis.format(t=t))

	def display_computers_board(self,board):
		'''This will display like display_own_board except
		with the ships masked'''
		xaxis = "   "
		for key, value in enumerate(board):
			new_row = "{t.normal}  " + str(key)
			for x in value:
				if x[1] == "M":
					new_row += "{t.normal}  |  {t.bold_blue}" + x[1]
				elif x[1] == "O":
					new_row += "{t.normal}  |  {t.normal}" + " "
				elif x[1] == "X":
					new_row += "{t.normal}  |  {t.bold_red}" + x[1]
				else:
					new_row += "{t.normal}  |  {t.normal}" + " "
			new_row += "{t.normal}  |"
			print(new_row.format(t=t))
			print("{t.normal}     -------------------------------------------------------------".format(t=t))
			xaxis += "     {t.normal}" + str(key)
		print(xaxis.format(t=t) +"\n")

	def place_ship(self,ship,active_player):
		os.system('clear')
		print(t.bold("WELCOME PLAYER - PLACE YOUR SHIPS!!\n"))
		#os.system('afplay gun.mp3')
		self.display_own_board(active_player.board.board)
		print ("Where would you like to place the {0}".format(ship.name))
		coordy,coordx,direction = None, None, None
		while coordx not in [str(x) for x in range(0,10)]:
			coordx = input("What is the x starting coordinate? ")
		while coordy not in [str(x) for x in range(0,10)]:
			coordy = input("What is the y starting coordinate? ")
		while direction not in ["l","r","d","u"]:
			direction = input("Direction: ")
		return int(coordx),int(coordy), direction

	def ask_coords(self,opposing_player,active_player):
		os.system('clear')
		print(opposing_player.name+"\n")
		self.display_computers_board(opposing_player.board.board)
		print(active_player.name+"\n")
		self.display_own_board(active_player.board.board)
		coordy = None
		coordx = None
		print("Where would you like to strike?")
		while coordx not in [str(x) for x in range(0,10)]:
			coordx = input("What is the x coordinate ")
		while coordy not in [str(x) for x in range(0,10)]:
			coordy = input("What is the y coordinate ")
		return int(coordy), int(coordx)

	def hit_miss(self, hit_miss,ship_sunk,opposing_player,active_player,coords):
		'''Displays boards, and relevant hit miss messages. This is always a 'human view'
		The computer's board will always be at the top (with obscured ships) 
		and the player's board at the bottom'''
		os.system('clear')
		if active_player.iscomputer == False:
			print(opposing_player.name+"\n")
			self.display_computers_board(opposing_player.board.board)
			print(active_player.name+"\n")
			self.display_own_board(active_player.board.board)
			if hit_miss == True and ship_sunk != None:
				print("You hit!")
				print("You sunk my " + ship_sunk + "!!!")
				os.system('afplay bomb.mp3')
			elif hit_miss == True:
				print("You hit")
				os.system('afplay shotgun.mp3')
			else:
				print ("You missed!")
				os.system('afplay woosh.mp3')
		else:
			#Fix coords
			print(active_player.name+"\n")
			self.display_computers_board(active_player.board.board)
			print(opposing_player.name+"\n")
			self.display_own_board(opposing_player.board.board)
			if hit_miss == True and ship_sunk != None:
				print("Computer hit at {0}".format(coords))
				print("You sunk my " + ship_sunk + "!!!")
				os.system('afplay bomb.mp3')
			elif hit_miss == True:
				print("Computer hit at {0}".format(coords))
				os.system('afplay shotgun.mp3')
			else:
				print ("Computer missed at{0}".format(coords))
				os.system('afplay woosh.mp3')
		enter = input("Press enter to continue ")


	def game_over(self,active_player_name):
		print("Congratulations!! {0} won the game".format(active_player_name))
		os.system('afplay win.mp3')