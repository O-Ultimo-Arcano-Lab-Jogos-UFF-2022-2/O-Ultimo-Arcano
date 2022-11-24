from src.classes.gameObjects.Enemy import Enemy
from src.pplay.sprite import Sprite

class Goblin(Enemy):
    
    def __init__(self, wave):
        super().__init__(wave)
        self.life = 10
        self.base_speed = [120, 120]
        self.speed = [0, 0]

        # @TODO Trocar o sprite
        self.gameObject = Sprite('./assets/images/player.png', 1)


    def loop(self):
        player = self.wave.game.player.gameObject
        window = self.wave.window

        self.speed = [0, 0]
        if (player.x != self.x):
            self.speed[0] = self.base_speed[0] if self.x < player.x else -self.base_speed[0]

        if (player.y != self.y):
            self.speed[1] = self.base_speed[1] if self.y < player.y else -self.base_speed[1]

        self.x += self.speed[0] * window.delta_time()
        self.y += self.speed[1] * window.delta_time()
      
  