import time
import pygame
from pygame.locals import *

from view import maping
from view import player
from view import screen

class Maze():
	blurImg = pygame.image.load('data/img/blur.png')

	def __init__(self, display):
		self.player = player.Player()
		self.map = maping.Map('data/maps/map.txt')
		
		# screen var
		self.DISPLAY_THREAD = display
		self.DISPLAY = self.DISPLAY_THREAD.get_display()
		
		# player's status var
		self.show_status = False
		self.show_inventory = False
		self.show_esc = False
		self.__status_list = []
		self.__inventory_list = []

		# font var
		self.fontObj = pygame.font.Font('freesansbold.ttf', 15)

	def continue_game(self, obj):
		self.player.set_player_status(obj[2])
		self.map.set_map_matrix(obj[1])

	def free_walk(self):
		fpsClock = pygame.time.Clock()
		fps = self.DISPLAY_THREAD.get_fps()

		while True:
			key = self.DISPLAY_THREAD.get_event()
			time.clock()

			if key == K_RIGHT:
				self.player.set_animation('right')
				temp_event = self.map.isPermitted(self.player.i , self.player.j, 'right')
				temp_event = temp_event.split('|')

				if temp_event[0] == 'empty':
					self.player.j += 1

				elif temp_event[0] == 'enemy':
					self.player.j += 1
					return ('ENEMY', temp_event[1])	# (event, type)

				elif temp_event[0] == 'win':
					return 'WINNER'

			elif key == K_LEFT:
				self.player.set_animation('left')
				temp_event = self.map.isPermitted(self.player.i , self.player.j, 'left')
				temp_event = temp_event.split('|')

				if temp_event[0] == 'empty':
					self.player.j -= 1

				elif temp_event[0] == 'enemy':
					self.player.j -= 1
					return ('ENEMY', temp_event[1])	# (event, type)

				elif temp_event[0] == 'win':
					return 'WINNER'

			elif key == K_DOWN:
				self.player.set_animation('down')
				temp_event = self.map.isPermitted(self.player.i , self.player.j, 'down')
				temp_event = temp_event.split('|')
				
				if temp_event[0] == 'empty':
					self.player.i += 1

				elif temp_event[0] == 'enemy':
					self.player.i += 1
					return ('ENEMY', temp_event[1])	# (event, type)

				elif temp_event[0] == 'win':
					return 'WINNER'

			elif key == K_UP:
				self.player.set_animation('up')
				temp_event = self.map.isPermitted(self.player.i , self.player.j, 'up')
				temp_event = temp_event.split('|')

				if temp_event[0] == 'empty':
					self.player.i -= 1

				elif temp_event[0] == 'enemy':
					self.player.i -= 1
					return ('ENEMY', temp_event[1])	# (event, type)

				elif temp_event[0] == 'win':
					return 'WINNER'

			elif key == K_i:
				if self.show_inventory:
					self.show_inventory = False
				else:
					self.show_inventory = True
					self.show_status = False

			elif key == K_s:
				if self.show_status:
					self.show_status = False
				else:
					self.show_status = True
					self.show_inventory = False

			elif key == K_ESCAPE:
				if self.show_esc:
					self.show_esc = False
				else:
					self.show_esc = True
					self.show_inventory = False
					self.show_status = False

			self.DISPLAY.fill((0,0,0))
			self.map.print_upper_part_map(self.DISPLAY)
			self.player.print_player(self.DISPLAY)
			self.map.print_lower_part_map(self.DISPLAY)
			self.DISPLAY.blit(self.blurImg, (0,0))

			if self.show_inventory:
				self.print_list(self.__inventory_list)

			elif self.show_status:
				self.print_list(self.__status_list)

			if self.show_esc:
				options_result = self.show_escape()

				if options_result == 'continue':
					self.show_esc = False

				elif options_result == 'save':
					return 'SAVE'

				elif options_result == 'exit':
					return 'END'

			text_obj = self.fontObj.render(str(time.clock()), True, (255,255,255), (0,0,0))
			self.DISPLAY.blit(text_obj, (20, 570))
			pygame.display.update()
			fpsClock.tick(fps)

	def set_status_list(self, myList):
		self.__status_list = myList

	def set_inventory_list(self, myList):
		self.__inventory_list = myList

	def print_list(self, myList):
		if len(myList) == 0:
			myList = ['empty']

		height = len(myList)
		width = len(max(myList, key = len))
		pygame.draw.rect(self.DISPLAY, (100, 100, 100), (10, 10, width * 11 + 10, height * 25))
		
		i = 1
		for element in myList:
			text_obj = self.fontObj.render(element, True, (255,255,255), (100,100,100))
			self.DISPLAY.blit(text_obj, (20, i * 20))
			i += 1

	def show_escape(self):
		option_y = 225
		bgColor = (100,100,100)
		charColor = (255,255,255)

		while True:
			key = self.DISPLAY_THREAD.get_event()
			
			if key == K_DOWN:
				if option_y == 265:
					option_y = 225
				else:
					option_y += 20

			elif key == K_UP:
				if option_y == 225:
					option_y = 265
				else:
					option_y -= 20

			elif key == K_ESCAPE:
				return 'continue'

			elif key == 13:
				if option_y == 265:
					return 'exit'

				elif option_y == 245:
					return 'save'

				else:
					return 'continue'

			pygame.draw.rect(self.DISPLAY, bgColor, (300, 200, 200, 100))
			text_obj = self.fontObj.render('Continuar', True, charColor, bgColor)
			self.DISPLAY.blit(text_obj, (330, 220))
			text_obj = self.fontObj.render('Salvar Jogo', True, charColor, bgColor)
			self.DISPLAY.blit(text_obj, (330, 240))
			text_obj = self.fontObj.render('Sair', True, charColor, bgColor)
			self.DISPLAY.blit(text_obj, (330, 260))
			pygame.draw.circle(self.DISPLAY, (0,0,0), (320, option_y), 3, 0)
			pygame.display.update()

	def win(self):
		winImg = pygame.image.load('data/img/win.png')
		self.DISPLAY.blit(winImg, (0, 0))
		pygame.display.update()
		time.sleep(5)

	def get_map(self):
		return self.map

	def get_player(self):
		return self.player