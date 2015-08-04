from view import player

class PlayerDAO:
	def __init__(self, PlayerObj):
		self.myPlayer = PlayerObj

	def get_player(self):
		return str(self.myPlayer.i) + "|" + str(self.myPlayer.j)