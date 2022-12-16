from src.classes.gameObjects.Collectible import Collectible


class LifeOrb(Collectible):
    hpHeal = 20

    def effect(self):
        self.player.currentHp += self.hpHeal
