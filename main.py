from control import controler

if __name__ == "__main__":
	try:
		game = controler.GameControl()
		game.begin()
	except:
		print('encerrando the maze...')