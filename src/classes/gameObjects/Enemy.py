from src.pplay.sprite import Sprite
from src.classes.utils.Vector import Vector
from src.classes.gameObjects.GameObjectInterface import GameObjectInterface

class Enemy(GameObjectInterface):
    def __init__(self, wave):
        self.speed: Vector

        self.wave = wave
        self.gameObject: Sprite = None
        self.life = 1


    def willBeInWindownEdge(self):
        window = self.wave.window

        nextPosition = (
            self.x + self.speed.x * window.delta_time(),
            self.y + self.speed.y * window.delta_time()
        )

        return (
            nextPosition[0] <= 5 or
            nextPosition[1] <= 5 or
            nextPosition[0] + self.width >= window.width - 5 or
            nextPosition[1] + self.height >= window.height - 5
        )

    def destroy(self):
        # Todo o algorítimo para tirar o inimigo da tela
        # e esconder.
        self.wave.destroyEnemy(self)

    
