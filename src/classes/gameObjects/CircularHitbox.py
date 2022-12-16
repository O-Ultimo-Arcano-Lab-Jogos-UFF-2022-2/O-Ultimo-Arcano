from typing import List
from src.classes.gameObjects.GameObjectInterface import GameObjectInterface
from src.classes.gameObjects.Hitbox import Hitbox

class CircularHitbox(Hitbox):

    def __init__(
        self, 
        radius: int | float, 
        targets: List[GameObjectInterface],
        duration = 1, 
        callback = None,
        sprite = None
    ):
        super().__init__(duration, sprite)
        self.targets = targets
        self.radius = radius
        self.callback = callback

    def collisions(self):
        c = [ 
            target for target in self.targets 
            if self.distanceTo(target, True) <= self.radius 
        ]
            
        return c

    def loop(self):
        super().loop()

        c = self.collisions()
        
        if (len(c) > 0  and self.callback):
            self.callback(c)
