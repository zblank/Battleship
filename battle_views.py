import os

class Views:
	def __init__(self):
		pass

	def display_own_board(self,board):
		os.system('clear')
		for x in board:
			print(x)
		print("")

	def display_computers_board(self,board):
		os.system('clear')

	def place_ship(self,ship):
		coordx = int(input("Starting coordinate? "))
		coordy = int(input("Starting coordinate? "))
		direction = input("Direction")
		return coordx, coordy, direction

	def ask_coords(self):
		coordy = None
		coordx = None
		while coordy not in range(0,10):
			coordy = int(input("What is the y coordinate"))
		while coordx not in range(0,10):
			coordx = int(input("What is the x coordinate"))
		return coordy, coordx

	def hit_miss(self, hit_miss):
		if hit_miss == True:
			print("You hit")
		else:
			print ("You missed")