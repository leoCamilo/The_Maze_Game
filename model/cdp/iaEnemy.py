import random

CHOICES_START = 0
CHOICES_END = 10

class IA_enemy():
	def __init__(self):
		self.MISS_ATACK = "miss_attack"
		self.RECOVER_LIFE = "recover_life"
		self.NORMAL_ATTACK = "attack"
		self.chance_MISS_ATTACK = 0
		self.chance_RECOVER_LIFE = 0

	def get_action(self):
		probability = random.randint(CHOICES_START, CHOICES_END)

		if (probability <= self.chance_MISS_ATTACK):
			return self.MISS_ATACK
		
		elif (probability <= self.chance_RECOVER_LIFE):
			return self.RECOVER_LIFE

		return self.NORMAL_ATTACK