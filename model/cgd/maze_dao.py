from model.cgd import maping_dao
from model.cgd import player_dao

class MazeObj:
	def __init__(self, mapObj, playerObj):
		self.mapObj = maping_dao.MapingDAO(mapObj).get_map()
		self.playerObj = player_dao.PlayerDAO(playerObj).get_player()

class MazeDAO:
	def __init__(self, maze):
		self.returnObj = MazeObj(maze.get_map(), maze.get_player())

	def get_maze_obj(self):
		return self.returnObj