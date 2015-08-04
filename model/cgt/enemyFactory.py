from model.cgt import directorEnemy
from model.cgt import mrSalaminhoBuilder
from model.cgt import srBilugoBuilder
from model.cgt import paulusBuilder
from model.cgt import piruletaBuilder
from model.cgt import reiDaCacimbinhaBuilder
from model.cgt import leposLepusBuilder

class EnemyFactory():
	def __init__(self):
		self.directorEnemy = directorEnemy.DirectorEnemy()

	def create_MrSalaminho(self):
		self.directorEnemy.setBuilder(mrSalaminhoBuilder.MrSalaminhoBuilder())
		return self.directorEnemy.createEnemy()

	def create_SrBilugo(self):
		self.directorEnemy.setBuilder(srBilugoBuilder.SrBilugoBuilder())
		return self.directorEnemy.createEnemy()

	def create_PAULUS(self):
		self.directorEnemy.setBuilder(paulusBuilder.PaulusBuilder())
		return self.directorEnemy.createEnemy()

	def create_piruleta(self):
		self.directorEnemy.setBuilder(piruletaBuilder.PiruletaBuilder())
		return self.directorEnemy.createEnemy()

	def create_rei_da_cacimbinha(self):
		self.directorEnemy.setBuilder(reiDaCacimbinhaBuilder.ReiDaCacimbinhaBuilder())
		return self.directorEnemy.createEnemy()

	def create_lepos_lepus(self):
		self.directorEnemy.setBuilder(leposLepusBuilder.LeposLepusBuilder)
		return self.directorEnemy.createEnemy()
