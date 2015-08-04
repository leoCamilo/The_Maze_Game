class Bag():
	def __init__(self):
		self.itens = []
	
	def add_item(self, item):
		if(item == None):
			return

		item.set_position(len(self.itens))
		self.itens += [item]
	
	def get_itens(self):
		return self.itens
	
	def get_bag_itens(self):
		bag_itens = []

		for item in self.itens :
			if(not(item.is_equipped())):
				bag_itens += [item]

		return bag_itens	

	def get_equiped_itens(self):
		bag_itens = []

		for item in self.itens :
			if(item.is_equipped()):
				bag_itens += [item]

		return bag_itens	
	
	def equip_item_position(self, position):
		self.itens[position].equip()
		return self.itens[position]
	
	def unequip_item_position(self, position):
		self.itens[position].unequip()
	
	def get_item_position(self, position):
		return self.itens[position]