from model.cdp import status
from model.cdp import bag

DEFAULT_NAME = "hero"
START_LVL = 0

class Personagem():
	def __init__(self):
		self.name = DEFAULT_NAME
		self.status = status.Status()
		self.bag = bag.Bag()
		self.arma = None
		self.munition = None

	def create(self, name):
		self.set_name(name)
		self.set_level(START_LVL)
		self.recover_full_life()

	def set_name(self, name):
		self.name = name

	def get_name(self):
		return self.name

	def get_level(self):
		return self.status.get_level()

	def set_level(self, level):
		self.status.set_level(level)

	def take_damage(self, damage):
		return self.status.take_damage(damage)

	def get_damage(self):
		return self.status.get_damage()

	def get_life(self):
		return self.status.get_life()

	def get_max_life(self):
		return self.status.get_max_life()

	def get_percent_life(self):
		return self.status.get_percent_life()

	def receive_XP(self, xp):
		if(self.status.receive_XP(xp)):
			return True

	def recover_life(self, life):
		self.status.recover_life(life)

	def recover_full_life(self):
		self.status.recover_full_life()

	def receive_item(self,item):
		self.bag.add_item(item)

	def get_itens_bag(self):
		return self.bag.get_bag_itens()

	def get_name_itens_bag(self):
		return self.bag.get_name_itens_bag();

	def get_equiped_itens(self):
		return self.bag.get_equiped_itens()

	def equip_arma(self, position):
		if(self.arma != None):
			self.status.rem_aditional_damage(self.arma.get_effect())

		self.arma = self.bag.equip_item_position(position)
		self.status.add_aditional_damage(self.arma.get_effect())

	def unequip_arma(self):
		if(self.arma != None):
			self.status.rem_aditional_damage(self.arma.get_effect())
			self.bag.unequip_item_position(self.arma.get_position())
			self.arma = None

	def equip_munition(self, position):
		if(self.munition != None):
			self.status.rem_aditional_damage(self.munition.get_effect())

		self.munition = self.bag.equip_item_position(position)
		self.status.add_aditional_damage(self.munition.get_effect())

	def unequip_munition(self):
		if(self.munition != None):
			self.status.rem_aditional_damage(self.munition.get_effect())
			self.bag.unequip_item_position(self.munition.get_position)
			self.munition = None
