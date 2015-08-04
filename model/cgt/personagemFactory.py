from model.cgt import itemFactory
from model.cdp import personagem

BAG_POSITION_GUN = 0
BAG_POSITION_AMMO = 1

class PersonagemFactory():
	item_factory = itemFactory.ItemFactory()
	PERSON_GUN = item_factory.create_bakugan_bow()
	PERSON_AMMO = item_factory.create_dart()

	def _init_(self):
		self.personagem = None
		
	def create_personagem(self, name):
		self.personagem = personagem.Personagem()
		self.personagem.create(name)
		self.personagem.receive_item(self.PERSON_GUN)
		self.personagem.receive_item(self.PERSON_AMMO)
		self.personagem.equip_arma(BAG_POSITION_GUN)
		self.personagem.equip_munition(BAG_POSITION_AMMO)
		return self.personagem