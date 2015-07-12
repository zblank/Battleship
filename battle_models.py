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
				l.append(['O','O'])
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

	def store_last_guess(self,coordinate=(0,0),whats_there="O",sunk=None):
		self.last_coordinate_chosen = coordinate
		self.last_coordinate_type = whats_there
		self.was_ship_sunk = sunk

	def check_coordinate(self,opposing_board,coord):
		y,x = coord
		if y >= 10 or y < 0 or x < 0 or x >= 10:
			return False
		elif opposing_board[y][x][1] in ["M","X"]:
			return False
		else:
			return True


	def choose_coordinates(self,opposing_player,count=1):
		'''takes the opposing player i.e the human, runs throuugh their board, and find's previous hits.
		It then looks up that particular ship in the list of remaining ships. If it still there i.e. not sunk
		it looks around the surrounding squares for a coordinate that hasn't already been chosen.
		Otherwise it picks a coordinate at random '''
		for row,columns in enumerate(opposing_player.board.board):
			for column,value in enumerate(columns):
				if opposing_player.board.board[row][column][0] in ["A","B","C","S","D"] and opposing_player.board.board[row][column][1] == "X":
					ship_type = opposing_player.board.board[row][column][0]
					for ship in opposing_player.ship_list:
						print(ship.short)
						print(ship_type)
						if ship_type == ship.short:
							x_or_y = random.choice(["x","y"])
							d = [x for x in range(1,count+1)] + [-x for x in range(1,count+1)]
							direction  = random.choice(d)
							if x_or_y == "y":
								row += direction
							elif x_or_y == "x":
								column += direction
							coordy = row
							coordx = column
							if self.check_coordinate(opposing_player.board.board,(coordy,coordx)) == True:
								return coordy, coordx
							else:
								count += 1
								return self.choose_coordinates(opposing_player,count)
		coordy = random.randint(0,9)
		coordx = random.randint(0,9)
		if self.check_coordinate(opposing_player.board.board,(coordy,coordx)) == True:
			return coordy, coordx
		else:
			return self.choose_coordinates(opposing_player)



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
			elif self.active_player.board.board[y][x][1] != "O":
				return False
		self.place_ship(get_coords,ship)
		return True


	def place_ship(self, get_coords,ship):
		''' places ships short symbol on coordinates '''
		for coord in get_coords:
			y,x = coord
			self.active_player.board.board[y][x][0], self.active_player.board.board[y][x][1] = ship.short, ship.short
		return True

	def guess(self,coords):
		y,x = coords
		whats_there = self.opposing_player.board.board[y][x][1]
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
				self.opposing_player.board.board[y][x][1] = "X"
				ship.remaining_pieces -= 1
			if ship.remaining_pieces != 0:
				new_ship_list.append(ship)
			else:
				ship_sunk = ship.name
		self.opposing_player.ship_list = new_ship_list
		return ship_sunk




	def miss(self,coords):
		y,x = coords
		self.opposing_player.board.board[y][x][1] = "M"





		
