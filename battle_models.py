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

	def choose_coordinates(self,ship):
		coordx = random.randint(0,9)
		coordy = random.randint(0,9)
		direction = random.choice(['u','d','l','r'])
		return coordx,coordy, direction


class Gameplay:
	def __init__(self):
		self.ship_list = [Ship("Battleship",4,"B1"),Ship("Destroyer",2,"D1")]
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
		print(get_coords)
		for coord in get_coords:
			y,x = coord
			if y >= 10 or y < 0 or x < 0 or x >= 10:
				return False
			if self.active_player.board.board[y][x] == "O":
				self.active_player.board.board[y][x] = ship.short
			else:
				return False
		print(self.active_player.board.board)
		return True
	
				




	def guess(self,coords):
		#search array
		# if not X,M,O:
		# 	self.hit(coords)
		# 	return True
		# else:
		# 	self.miss(coords)
		# 	return False
		pass



	def hit(self,coords):
		#find ship short e.g."D1"
		#change that spot to an x
		#reduce ship (e.g. D1) spots by 1
		#check if ship remaining spots = 0
		#check if ship_list length = 0
		pass


	def miss(self,coords):
		#change that spot to an M
		pass





		
