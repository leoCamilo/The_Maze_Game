from model.cdp import personagem
from model.cdp import iaEnemy
import random

MISS_ATACK = "miss_attack"
RECOVER_LIFE = "recover_life"

NO_DAMAGE = 0

CHANCES_START = 0
CHANCES_END = 10
DROP_CHANCE = 3

class Enemy(personagem.Personagem):
	def __init__(self):
		super().__init__()
		self.damage = 0
		self.life_multiplier = 0
		self.experience_reward = 0
		self.intelligence = None

	def get_action(self):	# execute a action returnig the damage taken by the player
		choice = self.intelligence.get_action()

		if (choice == MISS_ATACK):
			self.damage = NO_DAMAGE

		elif (choice == RECOVER_LIFE):
			self.recover_life(self.get_level() * self.life_multiplier)
			self.damage = NO_DAMAGE

		else:
			self.damage = self.get_damage()

		return self.damage

	def set_life_recover_mutiplier(self, life_multiplier):
		self.life_multiplier = self.life_multiplier

	def set_experience_reward(self, experience):
		self.experience_reward = experience

	def set_IA(self, IA):
		self.intelligence = IA;

	def get_experience_reward(self):
		return self.experience_reward

	def get_drop(self):
		chance = random.randint(CHANCES_START, CHANCES_END)

		if(chance <= DROP_CHANCE):
			itens = self.get_itens_bag()
			choice = random.randint(0, len(itens)-1)
			return itens[choice]

		return None
