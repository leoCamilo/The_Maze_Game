from model.cgt import enemyBuilder

class DirectorEnemy():  # receives a builder and return a enemy object
	def __init__(self):
		self.enemyBuilder = None

	def setBuilder(self, enemyBuilder):
		self.enemyBuilder = enemyBuilder

	def createEnemy(self):
		if(self.enemyBuilder == None):
			return None

		self.enemyBuilder.buildEnemy()
		self.enemyBuilder.buildItens()
		self.enemyBuilder.buildDrop()

		return self.enemyBuilder.getEnemy()