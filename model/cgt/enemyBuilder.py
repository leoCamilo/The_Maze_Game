from model.cdp import enemy
from model.cgt import itemFactory

class EnemyBuilder():   # [abstract]
	def __init__(self):
		self.enemy = enemy.Enemy()
		self.item_factory = itemFactory.ItemFactory()

	def buildEnemy(self):	# create basic enemy methods
		self.enemy.recover_full_life()

	def buildItens(self):	# create basic enemy itens 
		pass

	def buildDrop(self):	# create basic enemy drop 
		pass

	def getEnemy(self):		# return enemy object
		return self.enemy