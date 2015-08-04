from model.cdp import item

GUN = 1
AMMO = 2
USABLE = 3
ARTEFACT = 4

class ItemFactory():
	def __init__(self):
		self.item = None

	def create_simple_bow(self):
		self.item = item.Item()
		damage = 3
		self.item.create("Arco simples [+3]", GUN, damage)
		return self.item
		
	def create_bakugan_bow(self):
		self.item = item.Item()
		damage = 4
		self.item.create("Arco do Bakugan [+4]", GUN, damage)
		return self.item

	def create_sexy_pistol(self):
		self.item = item.Item()
		damage = 10
		self.item.create("Sexy Pistol [+10]", GUN, damage)
		return self.item
		
	def create_estilingue(self):
		self.item = item.Item()
		damage = 2
		self.item.create("Estilingue [+2]", GUN, damage)
		return self.item

	def create_dart_pistol(self):
		self.item = item.Item()
		damage = 6
		self.item.create("Pistola de dardos [+6]", GUN, damage)
		return self.item
	
	def create_dart_poison(self):
		self.item = item.Item()
		damage = 2
		self.item.create("Dardo envenenado [+2]", AMMO, damage)
		return self.item

	def create_dart(self):
		self.item = item.Item()
		damage = 1
		self.item.create("Dardo [+1]", AMMO, damage)
		return self.item

	def create_holly_bullet(self):
		self.item = item.Item()
		damage = 3
		self.item.create("Bala sagrada [+3]", AMMO, damage)
		return self.item

	def create_shit_monkey(self):
		self.item = item.Item()
		damage = 6
		self.item.create("Bosta de macaco [+6]", AMMO, damage)
		return self.item

	def create_brush(self):
		self.item = item.Item()
		damage = 1
		self.item.create("Pincel maroto [+1]", AMMO, damage)
		return self.item

	def create_paper_ball(self):
		self.item = item.Item()
		damage = 5
		self.item.create("Bolinha de papel [+5]", AMMO, damage)
		return self.item
	
	def create_low_health_potion(self):
		self.item = item.Item()
		heal = 3
		self.item.create("Pote de vida fraco [+3]", USABLE, heal)
		return self.item

	def create_medium_health_potion(self):
		self.item = item.Item()
		heal = 6
		self.item.create("Pote de vida mahomenos [+6]", USABLE, heal)
		return self.item
	
	def create_OP_health_potion(self):
		self.item = item.Item()
		heal = 12
		self.item.create("Pote de vida OVER POWER [+12]", USABLE, heal)
		return self.item

	def create_troll_health_potion(self):
		self.item = item.Item()
		heal = -5
		self.item.create("Pote de vida suprize []", USABLE, heal)
		return self.item