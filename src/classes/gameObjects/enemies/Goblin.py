from src.classes.gameObjects.Enemy import Enemy
from src.pplay.sprite import Sprite

class Goblin(Enemy):
    
    def __init__(self, wave):
        super().__init__(wave)
        self.life = 10
        self.gameObject = Sprite('./assets/images/player.png', 1)

    def loop(self):
        super().loop()
  