from src.pplay.sprite import Sprite
from src.classes.utils.Vector import Vector
from src.classes.gameObjects.projectiles.Projectile import Projectile

class GhostProjectile(Projectile):
    SPRITE_PATH = './assets/images/ghost_projectile.png'

    def __init__(self, game):
        super().__init__(
            game = game,
            damage = 12,
            targets = [ game.player.gameObject ],
            speed = Vector(0, 0),
            maxDistance = 750,
            sprite = Sprite(GhostProjectile.SPRITE_PATH, 1)
        )

    def launch(self):
        super().launch()

        direction = Vector \
            .fromObjects(self, self.game.player.gameObject) \
            .unit()

        self.speed = direction * 500

    def onColided(self, targets):
        self.destroy()
        self.game.player.takeHit(self.damage)