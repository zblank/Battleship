class Views:
	def __init__(self):
		pass

	def display_board(self):
		pass

	def place_ship(self,ship):
		coordx = int(input("Starting coordinate? "))
		coordy = int(input("Starting coordinate? "))
		direction = input("Direction")
		return coordx, coordy, direction

	def ask_coords(self):
		coordx = input("")
		coordy = input("")

	def hit_miss(self, hit_miss):
		if hit_miss == True:
			print("You hit")
		else:
			print ("You missed")