START_LEVEL = 0
START_LIFE = 0
START_ADITIONAL_DAMAGE = 0
START_EXPERIENCE = 0

NECESSARY_XP_MULTIPLIER = 50
STATIC_NECESSARY_XP = 25

LIFE_MULTIPLIER = 5
LIFE_STATIC_ADDITIONAL = 25

DMG_MULTIPLIER = 2;
DMG_STATIC_ADDITIONAL = 1

NEXT_LEVEL = 1
RECOVER_WHEN_LVL_UP = 3
NO_LIFE = 0

class Status():
	def __init__(self):
		self.level = START_LEVEL
		self.life = START_LIFE
		self.alive = True
		self.aditional_damage = START_ADITIONAL_DAMAGE
		self.experience = START_EXPERIENCE
	
		# change based on player level
		self.max_life = 10
		self.base_damage = 0
	
	def recover_full_life(self):
		self.life = self.max_life

	def recover_life(self, life):
		self.life += life
		
		if(self.life > self.max_life):
			self.life = self.max_life

	def take_damage(self, damage):	# returns true if player die
		self.life -= damage
		
		if(self.life <= NO_LIFE):
			self.alive = False
			self.life = 0
			return True

		return False

	def receive_XP(self, xp_received):	# returns true if player level up
		necessaryExperience = self.level * NECESSARY_XP_MULTIPLIER + STATIC_NECESSARY_XP
		self.experience += int(xp_received)
		
		if(self.experience >= necessaryExperience):
			self.experience -= necessaryExperience
			self.level_up()
			return True

		return False

	def level_up(self):
		self.set_level(self.level + NEXT_LEVEL)
		self.recover_life(self.level * RECOVER_WHEN_LVL_UP)

	def set_level(self,level):
		self.level = level
		self.max_life = level * LIFE_MULTIPLIER + LIFE_STATIC_ADDITIONAL
		self.base_damage = level * DMG_MULTIPLIER + DMG_STATIC_ADDITIONAL
	
	def set_aditional_damage(self, aditional_damage):	# by magic or item (ammo, potion, etc)
		self.aditional_damage = aditional_damage

	def add_aditional_damage(self, aditional):
		self.aditional_damage += aditional
	
	def rem_aditional_damage(self, aditional):
		self.aditional_damage = aditional
	
	def set_experience(self,xp):
		self.experience = xp
	
	def is_alive(self):
		return self.alive

	def get_life(self):
		return self.life

	def get_max_life(self):
		return self.max_life

	def get_percent_life(self):
		return self.life / self.max_life
		
	def get_damage(self):
		return self.base_damage + self.aditional_damage
	
	def get_level(self):
		return self.level