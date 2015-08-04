import sqlite3

class Dao:
	def __init__(self):
		self.conn = None
		self.cursor = None

	def connect(self):
		self.conn = sqlite3.connect('data/db/maze.db')
		self.cursor = self.conn.cursor()

	def close(self):
		self.conn.commit()
		self.conn.close()

	def saveOnDb(self, name):
		self.connect()
		sql = 'CREATE TABLE IF NOT EXISTS saves (name TEXT PRIMARY KEY, mapObj TEXT, playerObj TEXT)'
		self.cursor.execute(sql)
		
		try:
			sql = 'INSERT INTO saves (name, mapObj, playerObj) VALUES (?, ?, ?)'
			self.cursor.execute(sql, (name, 'none', 'none'))
			self.close()
		except sqlite3.IntegrityError:
			return

	def saveGame(self, name, obj):
		self.connect()		
		sql = 'UPDATE saves SET mapObj = ?, playerObj = ? WHERE name = \"' + name + '\"'
		self.cursor.execute(sql, (obj.mapObj, obj.playerObj))
		self.close()

	def getSaveByName(self, name):
		self.connect()
		sql = 'SELECT * FROM saves WHERE name = \"' + name + '\"'
		self.cursor.execute(sql)

		for line in self.cursor.fetchall():
			return line

		self.close()

	def viewDb(self):	# debug function
		self.connect()
		sql = 'SELECT name, playerObj FROM saves'
		self.cursor.execute(sql)

		for line in self.cursor.fetchall():
			print(line)

		self.close()