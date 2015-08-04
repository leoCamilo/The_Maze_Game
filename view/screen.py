import threading
import pygame, sys
from pygame.locals import *

class Screen(threading.Thread):
	SCREEN_WIDTH = 800
	SCREEN_HEIGHT = 600
	__display = None
	__FPS = 60
	__event = 0
	__event_type = 0
	__end = True

	def __init__(self):
		threading.Thread.__init__(self)

	def get_fps(self):
		return self.__FPS

	def get_display(self):
		while self.__display == None:
			pass

		return self.__display

	def get_event(self):
		temp_event = self.__event
		self.__event = 0
		return temp_event

	def get_event_type(self):
		temp_event_type = self.__event_type
		self.__event_type = 0
		return temp_event_type

	def run(self):
		pygame.init()
		pygame.display.set_caption('The Maze')
		self.__display = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), 0, 32)

		while self.__end:
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					self.__event_type = KEYDOWN
					self.__event = event.key

				elif event.type == QUIT:
					pygame.quit()
					sys.exit()

	def end(self):
		self.__end = False