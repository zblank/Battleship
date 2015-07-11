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
		self.ship_list = [Ship("Battleship",4,"B1"),Ship("Destroyer",2,"D1")]


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
		self.ship_list = [Ship("Battleship",4,"B1"),Ship("Destroyer",2,"D1")]

	def choose_starting_coordinates(self,ship):
		coordx = random.randint(0,9)
		coordy = random.randint(0,9)
		direction = random.choice(['u','d','l','r'])
		return coordx,coordy, direction

	def choose_coordinates(self):
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

	def place_ships(self,coordx,coordy,direction,ship):
		get_coords = self.get_proposed_coordinates(coordx,coordy,direction,ship.length)
		for coord in get_coords:
			y,x = coord
			if y >= 10 or y < 0 or x < 0 or x >= 10:
				return False
			if self.active_player.board.board[y][x] == "O":
				self.active_player.board.board[y][x] = ship.short
			else:
				return False
		return True

	def guess(self,coords):
		y,x = coords
		whats_there = self.opposing_player.board.board[y][x]
		if whats_there == "M":
			#Could implement a different message, but
			#for now just tell user they have missed
			return False
		elif whats_there == "X":
			#Could implement a different message, but
			#for now just tell user they have missed
			return False
		elif whats_there == "O":
			self.miss(coords)
			return False
		else:
			self.hit(coords,whats_there)
			return True

	def hit(self,coords,whats_there):
		ship_short = whats_there
		#Looks through the player's ship list,and amends
		y,x = coords
		new_ship_list = []
		for ship in self.opposing_player.ship_list:
			if ship.short == whats_there:
				self.opposing_player.board.board[y][x] = "X"
				ship.remaining_pieces -= 1
				if ship.remaining_pieces != 0:
					new_ship_list.append(ship)
				else:
					pass
					#pass some message to indicate ship sunk
		self.opposing_player.ship_list = new_ship_list




	def miss(self,coords):
		y,x = coords
		self.opposing_player.board.board[y][x] = "M"





		
