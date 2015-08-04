DEFAULT_NAME = "xablau"
DEFAULT_ITEM_TYPE = 0	# 1 - GUN | 2 - AMMO | 3 - USABLE | 4 - ARTEFACT

class Item():
	def __init__(self):
		self.name = DEFAULT_NAME
		self.effect = 0
		self.type_item = DEFAULT_ITEM_TYPE
		self.equipped = False
		self.position = 0

	def create(self, name, type_item, effect):
		self.name = name
		self.effect = effect
		self.type_item = type_item

	def get_effect(self):
		return self.effect
		
	def equip(self):
		self.equipped = True
		
	def unequip(self):
		self.equipped = False

	def is_equipped(self):
		return self.equipped

	def set_position(self, position):
		self.position = position
	
	def get_position(self, position):
		return self.position
		
	def get_name(self):
		return self.name

