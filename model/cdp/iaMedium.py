from model.cdp import iaEnemy

class IAMedium(iaEnemy.IA_enemy):
    def __init__(self):
        super().__init__()
        self.chance_RECOVER_LIFE = 4
        self.chance_MISS_ATTACK = 2