import threading
import time
import pygame, sys

from view import animationFactory
from pygame.locals import *
from view import screen

class Fight(threading.Thread):
	event = 0
	COLOR = (255, 255, 255)
	__end = True
	animation = False
	animation_type = 0
	call_ani_again = True

	life_hero = 350
	life_enemy = 350

	def __init__(self, display):
		threading.Thread.__init__(self)
		self.DISPLAY_THREAD = display
		self.DISPLAY = self.DISPLAY_THREAD.get_display()
		self.fontObj = pygame.font.Font('freesansbold.ttf', 15)
		self.life_hero_obj = self.fontObj.render('100', True, (0,200,0) ,self.COLOR)
		self.life_enemy_obj = self.fontObj.render('100', True, (0,200,0) ,self.COLOR)
		self.name_hero_obj = self.fontObj.render('X', True, (0,200,0) ,self.COLOR)
		self.name_enemy_obj = self.fontObj.render('X', True, (0,200,0) ,self.COLOR)
		self.animationClass = animationFactory.AnimationFactory()

	def run(self):
		fpsClock = pygame.time.Clock()
		display_elements = [
			pygame.image.load('data/animation/ani_1_1.png')
		]

		while self.__end: # the main game loop
			self.event = self.DISPLAY_THREAD.get_event()

			if self.animation == True and self.animation_type != 0:
				self.do_animation()

			self.DISPLAY.fill(self.COLOR)

			for element in display_elements:
				self.DISPLAY.blit(element, (200, 300))

			#print status bar
			self.print_status()

			pygame.display.update()
			fpsClock.tick(self.DISPLAY_THREAD.get_fps())

	def call_animation(self, ani_type):
		if self.call_ani_again:
			self.animation = True
			self.animation_type = ani_type
			self.call_ani_again = False
			return True
		else:
			return False

	def do_animation(self):
		animation_sprite_list = []
		default_time = 0.4

		if self.animation_type == animationFactory.CONST_ANIM_01:
			animation_time = default_time
			animation_sprite_list = self.animationClass.get_animation(animationFactory.CONST_ANIM_01)

		elif self.animation_type == animationFactory.CONST_ANIM_02:
			animation_time = default_time
			animation_sprite_list = self.animationClass.get_animation(animationFactory.CONST_ANIM_02)

		animation_time = animation_time / len(animation_sprite_list)

		for element in animation_sprite_list:
			self.DISPLAY.fill(self.COLOR)
			self.print_status()
			self.DISPLAY.blit(element, (200, 300))	# temporary
			pygame.display.update()
			time.sleep(animation_time)

		self.animation = False
		self.animation_type = 0
		self.call_ani_again = True

	def print_status(self):
		pygame.draw.rect(self.DISPLAY, (0, 200, 0), (10, 10, self.life_hero, 20))
		pygame.draw.rect(self.DISPLAY, (0, 200, 0), (790 - self.life_enemy, 10, self.life_enemy, 20))
		self.DISPLAY.blit(self.life_hero_obj, (10, 40))
		self.DISPLAY.blit(self.life_enemy_obj, (440, 40))
		self.DISPLAY.blit(self.name_hero_obj, (10, 60))
		self.DISPLAY.blit(self.name_enemy_obj, (440, 60))

	def get_event(self):
		temp_event = self.event
		self.event = 0
		return temp_event

	def set_life(self, player, modifier):	# modifier - percent
		if player == 'hero':
			self.life_hero = modifier * 350
		elif player == 'enemy':
			self.life_enemy = modifier * 350

	def set_num_life(self, player, string):
		if player == 'hero':
			self.life_hero_obj = self.fontObj.render(string, True, (0,200,0) ,self.COLOR)
		elif player == 'enemy':
			self.life_enemy_obj = self.fontObj.render(string, True, (0,200,0) ,self.COLOR)

	def set_player_name(self, player, name):
		if player == 'hero':
			self.name_hero_obj = self.fontObj.render(name, True, (0,200,0) ,self.COLOR)
		elif player == 'enemy':
			self.name_enemy_obj = self.fontObj.render(name, True, (0,200,0) ,self.COLOR)

	def game_over(self):
		while self.animation == True:
			pass

		self.print_status()
		loseImg = pygame.image.load('data/img/game_over.png')
		self.DISPLAY.blit(loseImg, (0, 0))
		pygame.display.update()
		time.sleep(5)

	def end(self):
		self.__end = False
		if self.animation_type != 0: #chama animação pendente, se houver
			self.do_animation() 