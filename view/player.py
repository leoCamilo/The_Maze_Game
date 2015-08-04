import pygame, sys
from pygame.locals import *

CENTER_SCREEN_X = 410
CENTER_SCREEN_y = 245
INITIAL_POSITION_ON_MATRIX_I = 0
INITIAL_POSITION_ON_MATRIX_J = 8

ANIMATION_DOWN = 1
ANIMATION_LEFT = 2
ANIMATION_RIGHT = 3
ANIMATION_UP = 4
ANIMATION_STOP = 0

START_SPRITE_DOWN = 1
START_SPRITE_LEFT = 5
START_SPRITE_RIGHT = 9
START_SPRITE_UP = 13

FINAL_SPRITE_DOWN = 4
FINAL_SPRITE_LEFT = 8
FINAL_SPRITE_RIGHT = 12
FINAL_SPRITE_UP = 16

NEXT_SPRITE = 1

class Player:
	def __init__(self):
		self.i = INITIAL_POSITION_ON_MATRIX_I
		self.j = INITIAL_POSITION_ON_MATRIX_J
		self.__pos_x = CENTER_SCREEN_X
		self.__pos_y = CENTER_SCREEN_y
		self.__animation = 0
		self.__animation_index = 1

		self.playerImg = {
			1 :  pygame.image.load('data/img/soldier/soldier (1).png'),
			2 :  pygame.image.load('data/img/soldier/soldier (2).png'),
			3 :  pygame.image.load('data/img/soldier/soldier (3).png'),
			4 :  pygame.image.load('data/img/soldier/soldier (4).png'),
			5 :  pygame.image.load('data/img/soldier/soldier (5).png'),
			6 :  pygame.image.load('data/img/soldier/soldier (6).png'),
			7 :  pygame.image.load('data/img/soldier/soldier (7).png'),
			8 :  pygame.image.load('data/img/soldier/soldier (8).png'),
			9 :  pygame.image.load('data/img/soldier/soldier (9).png'),
			10 : pygame.image.load('data/img/soldier/soldier (10).png'),
			11 : pygame.image.load('data/img/soldier/soldier (11).png'),
			12 : pygame.image.load('data/img/soldier/soldier (12).png'),
			13 : pygame.image.load('data/img/soldier/soldier (13).png'),
			14 : pygame.image.load('data/img/soldier/soldier (14).png'),
			15 : pygame.image.load('data/img/soldier/soldier (15).png'),
			16 : pygame.image.load('data/img/soldier/soldier (16).png')
		}

	def update(self):
		if self.__animation == ANIMATION_DOWN:
			if self.__animation_index == FINAL_SPRITE_DOWN:
				self.__animation_index = START_SPRITE_DOWN
				self.__animation = ANIMATION_STOP
			else:
				self.__animation_index += NEXT_SPRITE

		elif self.__animation == ANIMATION_LEFT:
			if self.__animation_index == FINAL_SPRITE_LEFT:
				self.__animation_index = START_SPRITE_LEFT
				self.__animation = ANIMATION_STOP
			else:
				self.__animation_index += NEXT_SPRITE

		elif self.__animation == ANIMATION_RIGHT:
			if self.__animation_index == FINAL_SPRITE_RIGHT:
				self.__animation_index = START_SPRITE_RIGHT
				self.__animation = ANIMATION_STOP
			else:
				self.__animation_index += NEXT_SPRITE

		elif self.__animation == ANIMATION_UP:
			if self.__animation_index == FINAL_SPRITE_UP:
				self.__animation_index = START_SPRITE_UP
				self.__animation = ANIMATION_STOP
			else:
				self.__animation_index += NEXT_SPRITE

	def set_animation(self, ani_type):
		if ani_type == 'left':
			self.__animation = ANIMATION_LEFT
			self.__animation_index = START_SPRITE_LEFT

		elif ani_type == 'right':
			self.__animation = ANIMATION_RIGHT
			self.__animation_index = START_SPRITE_RIGHT

		elif ani_type == 'up':
			self.__animation = ANIMATION_UP
			self.__animation_index = START_SPRITE_UP

		elif ani_type == 'down':
			self.__animation = ANIMATION_DOWN
			self.__animation_index = START_SPRITE_DOWN

		elif ani_type == 'center':
			self.__animation = ANIMATION_STOP
			self.__animation_index = START_SPRITE_DOWN

	def print_player(self, display):
		self.update()
		display.blit(self.playerImg[self.__animation_index], (self.__pos_x, self.__pos_y))

	def set_player_status(self, positions):
		if positions == 'none':
			return

		local = positions.split("|")
		self.i = int(local[0])
		self.j = int(local[1])