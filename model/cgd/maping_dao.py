from view import maping

class MapingDAO:
	def __init__(self, myMap):
		self.map_obj = myMap

	def get_map(self):
		saveMap = self.map_obj.get_map_obj()
		returnObj = ''

		for matrix_line in saveMap:
			for matrix_column in matrix_line:
				returnObj += matrix_column.element_type + '|' + str(matrix_column.pos_x) + '|' + str(matrix_column.pos_y) + '&'

		return returnObj			