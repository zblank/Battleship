import os

class Views:
	def __init__(self):
		pass

	def display_own_board(self,board):
		for x in board:
			print(x)
		print("")

	def display_computers_board(self,board):
		for x in board:
			print(x)
		print("")


	def place_ship(self,ship):
		coordy = int(input("What is the y starting coordinate? "))
		coordx = int(input("What is the x starting coordinate? "))
		direction = input("Direction: ")
		return coordx, coordy, direction

	def ask_coords(self):
		coordy = None
		coordx = None
		while coordy not in range(0,10):
			coordy = int(input("What is the y coordinate "))
		while coordx not in range(0,10):
			coordx = int(input("What is the x coordinate "))
		return coordy, coordx

	def hit_miss(self, hit_miss,opposing_player,active_player):
		print("{}'s View".format(active_player.name))
		print("")
		print(opposing_player.name)
		self.display_computers_board(opposing_player.board.board)
		print(active_player.name)
		self.display_own_board(active_player.board.board)
		if hit_miss == True:
			print("You hit!")
		else:
			print ("You missed!")