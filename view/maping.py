import pygame, sys
from pygame.locals import *

# x and y like a Cartesian plane
# but start to grow from the top left corner of the screen

WHITE_SPACE = ' '
WALL = '#'
END_GAME = 'F'
END_LINE = '\n'
END_LINE_2 = '\r'

class Map_element:
	def __init__(self, x, y, img, e_type):
		self.element_type = e_type
		self.img = img
		self.pos_x = x
		self.pos_y = y

	def __str__(self):
		return str(self.element_type) + str(self.pos_x) + " -- " + str(self.pos_y)

class Map:
	__enemy_list = ['1','2','3','4','5','6','7','8','9']	# character enemy representation, add here for new enemys

	__images = {
		WALL : pygame.image.load('data/img/Wood_Block_Tall.png'),
		WHITE_SPACE : pygame.image.load('data/img/Plain_Block.png'),
		END_GAME : pygame.image.load('data/img/Plain_Block.png'),
		__enemy_list[0] : pygame.image.load('data/img/enemies/Plain_Enemy1_Block.png'),
		__enemy_list[1] : pygame.image.load('data/img/enemies/Plain_Enemy2_Block.png'),
		__enemy_list[2] : pygame.image.load('data/img/enemies/Plain_Enemy3_Block.png'),
		END_LINE : pygame.image.load('data/img/empty.png'),
		END_LINE_2 : pygame.image.load('data/img/empty.png')
	}

	def __init__(self, path):
		self.__path = path
		self.__map_matrix = self.get_map_matrix()

	def get_map_matrix(self):	# this matrix is use to control colision on the map
		arq = open(self.__path,'rt')
		content = arq.readline()
		matrix = []
		line = []
		line_pos = 0
		column_pos = 6 	# start the column in six to put the map at the center of screen

		while content != '':
			for c in content:
				line.append(Map_element(line_pos * 50, column_pos * 40, self.__images[c], c))
				line_pos += 1

			matrix.append(line)
			line = []
			line_pos = 0
			column_pos += 1
			content = arq.readline()
 
		arq.close()
		return matrix

	# the player must appear above the map but the map part down him must appear above him
	def print_upper_part_map(self, display):
		for matrix_line in self.__map_matrix:
			if matrix_line[0].pos_y > 245:
				break

			for matrix_column in matrix_line:
				if matrix_column.pos_x < 150:
					continue

				elif matrix_column.pos_x > 650:
					break

				display.blit(matrix_column.img, (matrix_column.pos_x, matrix_column.pos_y))

	def print_lower_part_map(self, display):
		for matrix_line in self.__map_matrix:
			if matrix_line[0].pos_y < 245:
				continue

			if matrix_line[0].pos_y > 515:
				break

			for matrix_column in matrix_line:
				if matrix_column.pos_x < 150:
					continue

				elif matrix_column.pos_x > 650:
					break

				display.blit(matrix_column.img, (matrix_column.pos_x, matrix_column.pos_y))

	def move_map(self, x, y):
		for matrix_line in self.__map_matrix:
			for matrix_column in matrix_line:
				matrix_column.pos_x += x
				matrix_column.pos_y += y

	def isPermitted(self, line, column, direction):
		move_x = 0
		move_y = 0

		if direction == 'right':
			column += 1
			move_x = -50

		elif direction == 'left':
			column -= 1
			move_x = 50

		elif direction == 'down':
			line += 1
			move_y = -40

		elif direction == 'up':
			line -= 1
			move_y = 40

		else:
			return ''

		if self.__map_matrix[line][column].element_type == WHITE_SPACE:
			self.move_map(move_x, move_y)
			return 'empty'

		elif self.__map_matrix[line][column].element_type == END_GAME:
			self.move_map(move_x, move_y)
			return 'win'

		elif self.__map_matrix[line][column].element_type in self.__enemy_list:
			self.move_map(move_x, move_y)
			enemyType = self.__map_matrix[line][column].element_type
			self.__map_matrix[line][column].element_type = WHITE_SPACE
			self.__map_matrix[line][column].img = self.__images[WHITE_SPACE]
			return 'enemy|' + enemyType

		else:
			return ''

	def get_map_obj(self):
		return self.__map_matrix

	def set_map_matrix(self, listObj):
		if listObj == 'none':
			return

		mapList = listObj.split("&")
		mapList = mapList[:len(mapList) - 1]

		line_count = len(self.__map_matrix)
		column_count = len(self.__map_matrix[0])
		index = 0

		for line in range(line_count):
			for column in range(column_count):
				mapElem = mapList[index].split("|")
				self.__map_matrix[line][column] = Map_element(int(mapElem[1]), int(mapElem[2]), self.__images[mapElem[0]], mapElem[0])
				index += 1