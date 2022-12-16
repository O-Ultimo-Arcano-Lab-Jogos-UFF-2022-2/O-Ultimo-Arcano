from abc import ABC, abstractmethod
from random import randint
from src.pplay.sprite import Sprite


class Collectible(ABC):
    def __init__(self, window, player, sprite):
        self.window = window
        self.player = player
        self.gameObject = Sprite(sprite, 1)
        self.spawn()

    @abstractmethod
    def effect(self):
        pass

    def spawn(self):
        self.gameObject.x = randint(
            0, self.window.width - self.gameObject.width)
        self.gameObject.y = randint(
            0, self.window.height - self.gameObject.height)
