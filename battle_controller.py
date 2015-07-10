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

	def place(self):
		ship_list = self.game_play.ship_list
		for ship in ship_list:
			valid = False
			while valid == False: 
				if self.game_play.active_player.iscomputer == False:
					coordx, coordy, direction = self.v.place_ship(ship)
				else:
					coordx, coordy, direction = self.game_play.active_player.choose_coordinates(ship)
				valid = self.game_play.place_ships(coordx,coordy,direction,ship)


	def player_turn(self):
		pass
		# if human:
		# 	coords = views.guess()
		# else:
		# 	coords = models.guess(coords)
		# hit_miss = models.guess(coords)
		# views.hit_miss(hit_miss)
		# if game_over:
		# 	return self.game_over()
		# else:
		# 	self.active_player, self.opposing_player = self.opposing_player, self.active_player
		# 	self.player_turn()


	def game_over(self):
		pass

Controller()
		

