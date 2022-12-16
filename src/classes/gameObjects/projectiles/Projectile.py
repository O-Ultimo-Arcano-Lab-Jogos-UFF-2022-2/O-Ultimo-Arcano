
from src.classes.utils.Vector import Vector
from src.classes.gameObjects.GameObjectInterface import GameObjectInterface
from src.classes.utils.Vector import Vector
from src.classes.gameObjects.ProjectileManager import ProjectileManager

class Projectile(GameObjectInterface):
    def __init__(
        self,
        game, 
        damage, 
        targets, 
        speed, 
        maxDistance,
        sprite
    ): 
        super().__init__()

        self.game = game
        self.lauched = False
        self.origin = Vector(0, 0)

        self.damage = damage
        self.targets = targets
        self.maxDistance = maxDistance
        self.baseSpeed = speed
        self.speed = Vector(0, 0)
        self.gameObject = sprite

        ProjectileManager.add(self)

    def collisions(self):
        c = [ t for t in self.targets if self.collided(t) ]
        return c

    def destroy(self):
        ProjectileManager.remove(self)

    def launch(self):
        self.origin = Vector(self.x, self.y)
        self.speed = self.baseSpeed
    
    def loop(self):   
        window = self.game.window
        collisions = self.collisions()

        if (len(collisions) > 0):
            self.onColided(collisions)

        if (self.distanceTo(self.origin) >= self.maxDistance):
            self.destroy()
            return

        self.x += self.speed.x * window.delta_time()
        self.y += self.speed.y * window.delta_time()

    def onColided(self, targets): pass