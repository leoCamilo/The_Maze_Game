import unittest

from model import personagemFactory
from model import enemyFactory

from model.persist import DAO

class DbObj:
	def __init__(self):
		self.mapObj = 'test'
		self.playerObj = 'test'

class TestGame(unittest.TestCase):
	def test_player(self):
		factory_personagem = personagemFactory.PersonagemFactory()

		personagem = factory_personagem.create_personagem('paulus IV')
		self.assertEqual(personagem.get_name(), 'paulus IV')
		
		personagem.set_name('paulus V')
		self.assertEqual(personagem.get_name(), 'paulus V')

		self.assertEqual(personagem.get_level(), 0)

		player_life = str(personagem.get_life()) +"/"+ str(personagem.get_max_life())
		self.assertEqual(player_life, '25/25')

		personagem.set_level(1)
		self.assertEqual(personagem.get_level(), 1)

		player_life = str(personagem.get_life()) +"/"+ str(personagem.get_max_life())
		self.assertEqual(player_life, '25/30')

		personagem.recover_life(1)
		player_life = str(personagem.get_life()) +"/"+ str(personagem.get_max_life())
		self.assertEqual(player_life, '26/30')

		personagem.recover_full_life()
		player_life = str(personagem.get_life()) +"/"+ str(personagem.get_max_life())
		self.assertEqual(player_life, '30/30')

	def test_db(self):
		db = DAO.Dao()
		#db.saveOnDb('teste player')
		#self.assertEqual(db.getSaveByName('teste player'), ('teste player', 'none', 'none'))
		db.saveGame('teste player', DbObj())
		self.assertEqual(db.getSaveByName('teste player'), ('teste player', 'test', 'test'))

	# def test_upper(self):
	# 	self.assertEqual('foo'.upper(), 'FOO')

	# def test_isupper(self):
	# 	self.assertTrue('FOO'.isupper())
	# 	self.assertFalse('Foo'.isupper())

	# def test_split(self):
	# 	s = 'hello world'
	# 	self.assertEqual(s.split(), ['hello', 'world'])
	# 	# check that s.split fails when the separator is not a string
	# 	with self.assertRaises(TypeError):
	# 	s.split(2)

if __name__ == '__main__':
	unittest.main()