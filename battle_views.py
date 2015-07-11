import os

# You guys will have to install the blessings library
# if you don't already have it

from blessings import Terminal

t = Terminal()

class Views:
	def __init__(self):
		pass

	def display_own_board(self,board):
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

	def display_computers_board(self,board):
		for row in board:
			new_row = ''
			for x in row:
				new_row += "    " + x
			print(new_row)
			print("")


	def place_ship(self,ship,active_player):
		os.system('clear')
		print(t.bold("PLACE YOUR SHIPS!!"))
		self.display_own_board(active_player.board.board)
		print ("Where would you like to place the {0}".format(ship.name))
		coordy,coordx,direction = None, None, None
		while coordy not in range(0,10):
			coordy = int(input("What is the y starting coordinate? "))
		while coordx not in range(0,10):
			coordx = int(input("What is the x starting coordinate? "))
		while direction not in ["l","r","d","u"]:
			direction = input("Direction: ")
		return coordx, coordy, direction

	def ask_coords(self,opposing_player,active_player):
		os.system('clear')
		print("{}'s View".format(active_player.name))
		print("Where would you like to strike?")
		print("")
		print(opposing_player.name + "(this is where you are aiming")
		self.display_computers_board(opposing_player.board.board)
		print(active_player.name)
		self.display_own_board(active_player.board.board)
		coordy = None
		coordx = None
		while coordy not in range(0,10):
			coordy = int(input("What is the y coordinate "))
		while coordx not in range(0,10):
			coordx = int(input("What is the x coordinate "))
		return coordy, coordx

	def hit_miss(self, hit_miss,ship_sunk,opposing_player,active_player):
		
		os.system('clear')
		print("{}'s View".format(active_player.name))
		print("")
		print(opposing_player.name)
		self.display_computers_board(opposing_player.board.board)
		print(active_player.name)
		self.display_own_board(active_player.board.board)
		if hit_miss == True and ship_sunk != None:
			print("You hit!")
			print("You sunk my " + ship_sunk + "!!!")
		elif hit_miss == True:
			print("You hit")
		else:
			print ("You missed!")
		if active_player.iscomputer == False:
			enter = input("Press enter to continue ")

	def game_over(self,active_player_name):
		print("Congratulations!! {0} won the game".format(active_player))