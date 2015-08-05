from model.cgt import enemyBuilder
from model.cdp import iaDumb

LEVEL = 3
XP_REWARD = 75
RECOVER_MUTIPLIER = 1

BAG_POSITION_GUN = 0
BAG_POSITION_AMMO = 1

class MrSalaminhoBuilder(enemyBuilder.EnemyBuilder):
	def __init__(self):
		super().__init__()

	# OVERRIDE
	def buildEnemy(self):
		self.enemy.set_name("Mr Salaminho (lvl 3)")
		self.enemy.set_level(LEVEL)
		self.enemy.set_experience_reward(XP_REWARD)
		self.enemy.set_life_recover_mutiplier(RECOVER_MUTIPLIER)
		self.enemy.set_IA(iaDumb.IADumb())		
		super().buildEnemy()

	# OVERRIDE
	def buildItens(self):
		self.enemy.receive_item(self.item_factory.create_bakugan_bow())
		self.enemy.receive_item(self.item_factory.create_dart())
		self.enemy.equip_arma(BAG_POSITION_GUN)
		self.enemy.equip_munition(BAG_POSITION_AMMO)

	# OVERRIDE
	def buildDrop(self):
		self.enemy.receive_item(self.item_factory.create_low_health_potion())
		self.enemy.receive_item(self.item_factory.create_medium_health_potion())
		self.enemy.receive_item(self.item_factory.create_troll_health_potion())
		self.enemy.receive_item(self.item_factory.create_bakugan_bow())
