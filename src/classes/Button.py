from src.pplay.sprite import *

class Button:
    gameObject = None

    def __init__(self, assetPath, xPosition, yPosition):
        self.gameObject = Sprite(assetPath, 1)
        self.gameObject.x = xPosition
        self.gameObject.y = yPosition
