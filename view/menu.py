import pygame
from pygame.locals import *
from view import screen

KEY_ENTER = 13

OPTION_NEW_GAME = 390
OPTION_EXIT = 476

NEXT_OPTION = 43
NOT_CONFIRM = True

class Menu:
	def __init__(self, display):	
		# screen var
		self.DISPLAY_THREAD = display
		self.DISPLAY = self.DISPLAY_THREAD.get_display()
		self.fontObj = pygame.font.Font('freesansbold.ttf', 15)

	def show(self):
		fpsClock = pygame.time.Clock()
		fps = self.DISPLAY_THREAD.get_fps()
		playerName = ''
		white = (255, 255, 255)
		black = (0, 0, 0)
		key = 0

		while NOT_CONFIRM:
			type_event = self.DISPLAY_THREAD.get_event_type()
			
			if type_event == KEYDOWN:
				key = self.DISPLAY_THREAD.get_event()
				
				if key == K_BACKSPACE:
					playerName = playerName[:len(playerName)-1]

				elif key == KEY_ENTER:
					break

				else:
					playerName += chr(key)

			self.DISPLAY.fill(white)
			text_obj = self.fontObj.render('Digite seu nome: ' + playerName, True, (0,0,0), white)
			self.DISPLAY.blit(text_obj, (20, 20))
			pygame.display.update()
			fpsClock.tick(fps)

		menuImg = pygame.image.load('data/img/title.png')
		option_y = OPTION_NEW_GAME

		while NOT_CONFIRM:
			key = self.DISPLAY_THREAD.get_event()
			
			if key == K_DOWN:
				if option_y == OPTION_EXIT:
					option_y = OPTION_NEW_GAME
				else:
					option_y += NEXT_OPTION

			elif key == K_UP:
				if option_y == OPTION_NEW_GAME:
					option_y = OPTION_EXIT
				else:
					option_y -= NEXT_OPTION

			elif key == KEY_ENTER:
				if option_y == OPTION_NEW_GAME:
					return 'new|' + playerName

				elif option_y == OPTION_EXIT:
					return 'exit|' + playerName

				else:
					return 'continue|' + playerName

			self.DISPLAY.fill(white)
			self.DISPLAY.blit(menuImg, (0, 0))
			pygame.draw.circle(self.DISPLAY, black, (325, option_y), 5, 0)
			pygame.display.update()
			fpsClock.tick(fps)