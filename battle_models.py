import random

class Database:
	pass

class Board:
	def __init__(self,size=10):
		self.size = size
		self.board = self.create_board()

	def create_board(self):
		final_list = []
		for num in range(self.size):
			l = []
			for num in range(self.size):
				l.append('O')
			final_list.append(l)
		return final_list



class Player:
	def __init__(self, name):
		self.name = name
		self.board = Board()
		self.iscomputer = False
		self.store_last_guess()
		self.ship_list = [Ship("Aircraft Carrier",5,"A"), Ship("Battleship",4,"B"), Ship("Cruiser",3,"C"), Ship("Submarine",3,"S"), Ship("Destroyer",2,"D")]

	def store_last_guess(self,coordinate=(0,0),whats_there="O",sunk=False):
		self.last_coordinate_chosen = coordinate
		self.last_coordinate_type = whats_there
		self.was_ship_sunk = sunk


class Ship:
	def __init__(self,name,length,short):
		self.name = name
		self.length = length
		self.short = short
		self.remaining_pieces = length




class Computer:
	def __init__(self, name):
		self.name = name
		self.board = Board()
		self.iscomputer = True
		self.store_last_guess()
		self.ship_list = [Ship("Aircraft Carrier",5,"A"), Ship("Battleship",4,"B"), Ship("Cruiser",3,"C"), Ship("Submarine",3,"S"), Ship("Destroyer",2,"D")]

	def choose_starting_coordinates(self,ship):
		coordx = random.randint(0,9)
		coordy = random.randint(0,9)
		direction = random.choice(['u','d','l','r'])
		return coordx,coordy, direction

	# def choose_coordinates(self):
	# 	coordy = random.randint(0,9)
	# 	coordx = random.randint(0,9)
	# 	return coordy, coordx

	def store_last_guess(self,coordinate=(0,0),whats_there="O",sunk=None):
		self.last_coordinate_chosen = coordinate
		self.last_coordinate_type = whats_there
		self.was_ship_sunk = sunk

	def choose_coordinates(self):
		print(self.last_coordinate_chosen,self.last_coordinate_type,self.was_ship_sunk)
		coordy,coordx = self.last_coordinate_chosen
		if self.last_coordinate_type in ["A","B","C","S","D"] and self.was_ship_sunk == None:
			x_or_y = random.choice(["x","y"])
			direction  = random.choice([-1,1])
			if x_or_y == "y":
				coordy += direction
			elif x_or_y == "x":
				coordx += direction
			if coordx < 0 or coordx > 9 or coordy < 0 or coordy > 9:
				return self.choose_coordinates()
			return coordy, coordx
		else:
			coordy = random.randint(0,9)
			coordx = random.randint(0,9)
			return coordy, coordx




class Gameplay:
	def __init__(self):
		self.active_player = Player("Player 1")
		self.opposing_player = Computer("Computer")

	def switch_players(self):
		self.active_player, self.opposing_player = self.opposing_player,self.active_player

	def get_proposed_coordinates(self,coordx,coordy,direction,ship):
		''' Takes a starting coordinate, direction, and a ship
			and returns a list of implied coordinates [y,x]'''
		coord_list = [(coordy,coordx)]
		for x in range(ship-1):
			if direction == 'd':
				coordy += 1
				coord_list.append([coordy,coordx])
			elif direction == 'u':
				coordy -= 1
				coord_list.append([coordy,coordx])
			elif direction == 'l':
				coordx -= 1
				coord_list.append([coordy,coordx])
			elif direction == 'r':
				coordx += 1
				coord_list.append([coordy,coordx])
		return coord_list

	def check_valid_coordinates(self,coordx,coordy,direction,ship):
		''' gets coordinates based on get_proposed_coordinates and checks 
			if they are valid. If True, proceed to place_ships and returns True
			else, returns False '''
		get_coords = self.get_proposed_coordinates(coordx,coordy,direction,ship.length)
		for coord in get_coords:
			y,x = coord
			if y >= 10 or y < 0 or x < 0 or x >= 10:
				return False
			elif self.active_player.board.board[y][x] != "O":
				return False
		self.place_ship(get_coords,ship)
		return True


	def place_ship(self, get_coords,ship):
		''' places ships short symbol on coordinates '''
		for coord in get_coords:
			y,x = coord
			self.active_player.board.board[y][x] = ship.short
		return True

	def guess(self,coords):
		y,x = coords
		whats_there = self.opposing_player.board.board[y][x]
		if whats_there == "M":
			#Could implement a different message, but
			#for now just tell user they have missed
			self.active_player.store_last_guess(coords,whats_there,False)
			return False, None
		elif whats_there == "X":
			#Could implement a different message, but
			#for now just tell user they have missed
			self.active_player.store_last_guess(coords,whats_there,False)
			return False, None
		elif whats_there == "O":
			self.miss(coords)
			self.active_player.store_last_guess(coords,whats_there,False)
			return False, None
		else:
			ship_sunk = self.hit(coords,whats_there)
			self.active_player.store_last_guess(coords,whats_there,ship_sunk)
			return True, ship_sunk


	def hit(self,coords,whats_there):
		''' Once a hit has been determined, changes
		that coordinate to an "X", and removes one piece 
		from the ship object. If the ship's length is zero it is
		not added to the updated ship list i.e. removed and a message
		is passed to the guess function that the ship has been sunk '''
		ship_short = whats_there
		#Looks through the player's ship list,and amends
		y,x = coords
		new_ship_list = []
		ship_sunk = None
		for ship in self.opposing_player.ship_list:
			if ship.short == whats_there:
				self.opposing_player.board.board[y][x] = "X"
				ship.remaining_pieces -= 1
			if ship.remaining_pieces != 0:
				new_ship_list.append(ship)
			else:
				ship_sunk = ship.name
		self.opposing_player.ship_list = new_ship_list
		return ship_sunk




	def miss(self,coords):
		y,x = coords
		self.opposing_player.board.board[y][x] = "M"





		
