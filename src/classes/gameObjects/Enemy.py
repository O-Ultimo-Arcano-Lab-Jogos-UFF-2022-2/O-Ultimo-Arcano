from src.pplay.sprite import Sprite
from src.classes.utils.Vector import Vector
from src.classes.gameObjects.GameObjectInterface import GameObjectInterface
from src.classes.gameObjects.Hitbox import Hitbox


class Enemy(GameObjectInterface):
    absoluteInvincibilityCooldown = 0.2

    def __init__(self, wave):
        super().__init__()

        self.speed: Vector
        self.wave = wave
        self._life = self.MAX_HP
        self.hitbox = Hitbox(None)
        self.hitbox.width = self.width
        self.hitbox.height = self.height
        self.collisionDamage = 10
        self.invincibilityCooldown = 0
        self.needsToBeDrawn = True
        self.invencible = False

    @property
    def life(self):
        return self._life

    @life.setter
    def life(self, value):
        self._life = max(0, min(value, self.MAX_HP))
        

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

    def handlePlayerCollision(self):
        player = self.wave.game.player
        player.takeHit(self.collisionDamage)

    def takeHit(self, damage):
        if (self.invincibilityCooldown == 0):
            self.needsToBeDrawn = False
            self.invincibilityCooldown = self.absoluteInvincibilityCooldown

            self.life -= damage

            if self.life == 0:
                self.destroy()

    def destroy(self):
        # Todo o algorítimo para tirar o inimigo da tela
        # e esconder.
        self.wave.destroyEnemy(self)

    def loop(self):
        player = self.wave.game.player
        self.hitbox.x = self.x
        self.hitbox.y = self.y
        self.hitbox.width = self.width
        self.hitbox.height = self.height

        if (self.hitbox.enabled):
            if (len(self.hitbox.collisions([player.gameObject]))):
                self.handlePlayerCollision()

        if (self.invincibilityCooldown != 0):
            self.needsToBeDrawn = not self.needsToBeDrawn
            self.invincibilityCooldown = max(
                self.invincibilityCooldown - self.wave.window.delta_time(), 0)
        else:
            self.needsToBeDrawn = True
