from model.cdp import iaEnemy

class IADumb(iaEnemy.IA_enemy):
    def __init__(self):
        super().__init__()
        self.chance_RECOVER_LIFE = 5
        self.chance_MISS_ATTACK = 5