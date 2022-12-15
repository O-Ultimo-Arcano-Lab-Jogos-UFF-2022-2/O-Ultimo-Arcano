from abc import abstractmethod
from src.classes.gameObjects.GameObjectInterface import GameObjectInterface
from typing import List
from src.classes.gameObjects.HitboxManager import HitboxManager

class Hitbox(GameObjectInterface):

    def __init__(self, duration = 1, sprite = None):
        super().__init__()
        
        """ Temporário """
        self.gameObject = sprite
        self.initialWidth: int | float = 0
        self.initialHeight: int | float = 0
        self.duration = duration
        HitboxManager.add(self)

    """ Dimensiona a hitbox mantendo o centro
    na mesma posição """
    def scale(self, scaleFactor: int | float, useInitial = True):
        coordFactor = 1 if scaleFactor < 1 else -1
        width = self.initialWidth if useInitial else self.width
        height = self.initialHeight if useInitial else self.height

        self.width = width * scaleFactor
        self.height = height * scaleFactor
        self.x += self.width / 2 * coordFactor
        self.y += self.height / 2 * coordFactor

    def loop(self):
        super().loop()

        if (self.duration == 0):
            self.destroy()

        self.duration -= 1
        

    def destroy(self):
        super().destroy()
        HitboxManager.remove(self)


    @abstractmethod
    def collided(self, targets: List[GameObjectInterface], callback = None): pass