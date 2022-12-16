from src.classes.gameObjects.collectibles.LifeOrb import LifeOrb


class CollectiblesManager():
    maxCollectibles = 3
    absoluteSpawnCooldown = 15

    def __init__(self, window, player):
        self.window = window
        self.player = player
        self.collectibles = []
        self.spawnCooldown = 0

    def loop(self):
        self.spawnCooldown = max(
            self.spawnCooldown - self.window.delta_time(), 0)
        shouldSpawnCollectible = self.player.currentHp < self.player.maxHp

        if (shouldSpawnCollectible and self.spawnCooldown == 0 and len(self.collectibles) < self.maxCollectibles):
            self.spawnCooldown = self.absoluteSpawnCooldown
            self.collectibles.append(
                LifeOrb(self.window, self.player, "./assets/images/life_orb.png"))

        for collectible in self.collectibles:
            if self.player.gameObject.collided(collectible.gameObject):
                collectible.effect()
                self.collectibles.remove(collectible)

    def draw(self):
        for collectible in self.collectibles:
            collectible.gameObject.draw()
