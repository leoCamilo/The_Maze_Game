from model.cgt import enemyBuilder

LEVEL = 2
XP_REWARD = 40
RECOVER_MUTIPLIER = 2

BAG_POSITION_GUN = 0
BAG_POSITION_AMMO = 1

class PiruletaBuilder(enemyBuilder.EnemyBuilder):
	def __init__(self):
		super().__init__()

	# OVERRIDE
	def buildEnemy(self):
		self.enemy.set_name("Piruleta (lvl 2)")
		self.enemy.set_level(LEVEL)
		self.enemy.set_experience_reward(XP_REWARD)
		self.enemy.set_life_recover_mutiplier(RECOVER_MUTIPLIER)
		super().buildEnemy()

	# OVERRIDE
	def buildItens(self):
		self.enemy.receive_item(self.item_factory.create_estilingue())
		self.enemy.receive_item(self.item_factory.create_dart_pistol())
		self.enemy.equip_arma(BAG_POSITION_GUN)
		self.enemy.equip_munition(BAG_POSITION_AMMO)

	# OVERRIDE
	def buildDrop(self):
		self.enemy.receive_item(self.item_factory.create_estilingue())
		self.enemy.receive_item(self.item_factory.create_dart_pistol())
		self.enemy.receive_item(self.item_factory.create_medium_health_potion())
