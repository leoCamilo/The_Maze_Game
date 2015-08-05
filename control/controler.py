from view import maze
from view import battle
from view import screen
from view import menu

from model.cgd import maze_dao
from model.cgd import DAO

from model.cgt import personagemFactory
from model.cgt import enemyFactory

CONST_OPTION = 0
CONST_NAME_HERO = 1
CONST_OPT_SPLIT = '|'

CONST_KEY_W = 119
CONST_KEY_ESCAPE = 27

CONST_HERO = 'hero'
CONST_ENEMY = 'enemy'

CONST_ANI_1 = 'hero_atack'
CONST_ANI_2 = 'enemy_atack'

class GameControl:
	def __init__(self):
		self.display = screen.Screen()
		self.display.start()
		self.maze_game = maze.Maze(self.display)
		self.initial_menu = menu.Menu(self.display)
		self.factory_personagem = personagemFactory.PersonagemFactory()
		self.personagem = None
		self.factory_enemy = enemyFactory.EnemyFactory()

	def show_menu(self):
		option = self.initial_menu.show()
		option = option.split(CONST_OPT_SPLIT)
		self.personagem = self.factory_personagem.create_personagem(option[CONST_NAME_HERO])
		db = DAO.Dao()
		db.saveOnDb(self.personagem.get_name())
		return option[CONST_OPTION]

	def begin(self):
		choice = self.show_menu()

		if choice == 'new':
			self.start_game()

		elif choice == 'continue':
			db = DAO.Dao()
			continueObj = db.getSaveByName(self.personagem.get_name())

			if continueObj != None:
				self.maze_game.continue_game(continueObj)

			self.start_game()

		elif choice == 'exit':
			self.end_game()

	def set_person_data(self):
		life = "life : " + str(self.personagem.get_life()) + "/" + str(self.personagem.get_max_life())
		level = "level : " + str(self.personagem.get_level())

		self.maze_game.set_status_list([life, level])
		self.maze_game.set_inventory_list(self.personagem.get_name_itens_bag())

	def start_game(self):
		self.set_person_data()

		while True:
			map_event = self.maze_game.free_walk()

			if map_event[0] == 'ENEMY':			# if is a enemy event
				if self.enemy_event(map_event[1]) == 'lose':
					return

			elif map_event == 'WINNER':
				self.win_game()
				return

			elif map_event == 'END':
				self.end_game()
				return

			elif map_event == 'SAVE':
				db = DAO.Dao()
				obj = maze_dao.MazeDAO(self.maze_game)
				db.saveGame(self.personagem.get_name(), obj.get_maze_obj())

	def enemy_event(self, enemyType):
		fight = battle.Fight(self.display)
		fight.start()

		if(enemyType == '1'):
			enemy = self.factory_enemy.create_SrBilugo()

		elif(enemyType == '2'):
			enemy = self.factory_enemy.create_piruleta()

		elif(enemyType == '3'):
			enemy = self.factory_enemy.create_rei_da_cacimbinha()

		fight.set_num_life(CONST_HERO, str(self.personagem.get_life()) + "/" + str(self.personagem.get_max_life()))
		fight.set_life(CONST_HERO, self.personagem.get_percent_life())
		fight.set_player_name(CONST_HERO, str(self.personagem.get_name()) + ' (lvl '+ str(self.personagem.get_level()) + ')')

		fight.set_num_life(CONST_ENEMY, str(enemy.get_life()) + "/" + str(enemy.get_max_life()))
		fight.set_life(CONST_ENEMY, enemy.get_percent_life())
		fight.set_player_name(CONST_ENEMY, enemy.get_name())

		while True:
			key_event = fight.get_event()

			if key_event == CONST_KEY_W:
				if(enemy.take_damage(self.personagem.get_damage())):
					if(self.personagem.receive_XP(enemy.get_experience_reward())):
						#self.personagem.get_level() #retorna novo lvl da criança
						self.set_person_data()
						pass

					drop = enemy.get_drop()
					self.personagem.receive_item(drop)

					while not fight.call_animation(CONST_ANI_1):
						pass

					fight.set_num_life(CONST_HERO, str(self.personagem.get_life()) + "/" + str(self.personagem.get_max_life()))
					fight.set_life(CONST_HERO, self.personagem.get_percent_life())
					fight.set_num_life(CONST_ENEMY, "0/" + str(enemy.get_max_life()))
					enemy = None
					fight.end()
					break

				while not fight.call_animation(CONST_ANI_1):
					pass

				fight.set_num_life(CONST_ENEMY, str(enemy.get_life()) + '/' + str(enemy.get_max_life()))
				fight.set_life(CONST_ENEMY, enemy.get_percent_life())

				if(self.personagem.take_damage(enemy.get_action())):
					while not fight.call_animation(CONST_ANI_2):
						pass

					fight.set_num_life(CONST_HERO, "0/" + str(self.personagem.get_max_life()))
					fight.set_life(CONST_HERO, 0)
					fight.set_player_name(CONST_HERO, str(self.personagem.get_name()) + ' (lvl ' + str(self.personagem.get_level()) + ')')

					fight.set_num_life(CONST_ENEMY, str(enemy.get_life()) + "/" + str(enemy.get_max_life()))
					fight.set_life(CONST_ENEMY, enemy.get_percent_life())
					fight.set_player_name('enemy', enemy.get_name())

					fight.end()
					fight.game_over()
					self.display.end()
					return 'lose'

				while not fight.call_animation(CONST_ANI_2):
					pass

				fight.set_num_life(CONST_HERO, str(self.personagem.get_life()) + "/" + str(self.personagem.get_max_life()))
				fight.set_life(CONST_HERO, self.personagem.get_percent_life())

			if key_event == CONST_KEY_ESCAPE:
				fight.end()
				break

		return 'win'

	def win_game(self):
		self.maze_game.win()
		self.display.end()

	def end_game(self):
		print('Saindo...')
		self.display.end()
