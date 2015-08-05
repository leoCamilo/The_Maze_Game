from model.cgt import enemyBuilder
from model.cdp import iaSmartBitch

LEVEL = 7
XP_REWARD = 120
RECOVER_MUTIPLIER = 3

BAG_POSITION_GUN = 0
BAG_POSITION_AMMO = 1

class ReiDaCacimbinhaBuilder(enemyBuilder.EnemyBuilder):
	def __init__(self):
		super().__init__()

	# OVERRIDE
	def buildEnemy(self):
		self.enemy.set_name("Rei da Cacimbinha (lvl 7)")
		self.enemy.set_level(LEVEL)
		self.enemy.set_experience_reward(XP_REWARD)
		self.enemy.set_life_recover_mutiplier(RECOVER_MUTIPLIER)
		self.enemy.set_IA(iaSmartBitch.IASmartBitch())
		super().buildEnemy()

	# OVERRIDE
	def buildItens(self):
		self.enemy.receive_item(self.item_factory.create_sexy_pistol())
		self.enemy.receive_item(self.item_factory.create_shit_monkey())
		self.enemy.equip_arma(BAG_POSITION_GUN)
		self.enemy.equip_munition(BAG_POSITION_AMMO)

	# OVERRIDE
	def buildDrop(self):
		self.enemy.receive_item(self.item_factory.create_sexy_pistol())
		self.enemy.receive_item(self.item_factory.create_shit_monkey())
		self.enemy.receive_item(self.item_factory.create_shit_monkey())
