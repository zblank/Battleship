import battle_models as m
import battle_views

class Controller:
	def __init__(self):
		self.game_play = m.Gameplay()
		self.v = battle_views.Views()
		self.start()

	def start(self):
		self.place()
		self.game_play.switch_players()
		self.place()
		self.game_play.switch_players()
		self.player_turn()

	def place(self):
		'''For every ship in the player's ship list, asks user
		(player or computer) for coordinates and direction. If valid,
		it places the ship there, otherwise asks them again'''
		ship_list = self.game_play.active_player.ship_list
		for ship in ship_list:
			valid = False
			while valid == False: 
				if self.game_play.active_player.iscomputer == False:
					#Passes the views both the ship and the player, so that they can view their
					#board before placing
					coordx, coordy, direction = self.v.place_ship(ship,self.game_play.active_player)
				else:
					coordx, coordy, direction = self.game_play.active_player.choose_starting_coordinates(ship)
				valid = self.game_play.check_valid_coordinates(coordx,coordy,direction,ship)

	def player_turn(self):
		'''If the computer is a human it takes input values from the player, otherwise it uses the Computer's
		choose_coordinates function. Calls on the relevant views functions to announce a hit or miss.
		Then tests for whether the ship list is empty, and if so announces game over. Otherwise, switches switch_players
		and repeats '''
		if self.game_play.active_player.iscomputer == True:
			coords = self.game_play.active_player.choose_coordinates(self.game_play.opposing_player)
		else:
			coords = self.v.ask_coords(self.game_play.opposing_player,self.game_play.active_player)
		hit_miss, ship_sunk = self.game_play.guess(coords)
		self.v.hit_miss(hit_miss, ship_sunk, self.game_play.opposing_player,self.game_play.active_player,coords)
	
		if self.game_play.opposing_player.ship_list == []:
			return self.game_over()
		else:
			self.game_play.switch_players()
			return self.player_turn()


	def game_over(self):
		self.v.game_over(self.game_play.active_player.name)

Controller()
		

