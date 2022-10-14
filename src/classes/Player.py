from src.pplay.sprite import *

class Player:
    window = None
    keyboard = None
    gameObject = None
    absoluteSpeed = 400
    xSpeed = None
    ySpeed = None
    moveUpKeybind = "UP"
    moveDownKeybind = "DOWN"
    moveLeftKeybind = "LEFT"
    moveRightKeybind = "RIGHT"

    def __init__(self, window, keyboard):
        self.window = window
        self.keyboard = keyboard
        self.gameObject = Sprite("./assets/images/player.png", 1)

        self.gameObject.x = (self.window.width / 2) - (self.gameObject.width / 2)
        self.gameObject.y = (self.window.height / 2) - (self.gameObject.height / 2)

        self.absoluteSpeed = self.absoluteSpeed
        self.xSpeed = self.absoluteSpeed
        self.ySpeed = self.absoluteSpeed

    def control(self, offset):
        worldOffset = offset

        if (self.keyboard.key_pressed(self.moveUpKeybind)):
            worldOffset[1] += self.moveUp()

        if (self.keyboard.key_pressed(self.moveDownKeybind)):
            worldOffset[1] += self.moveDown()

        if (self.keyboard.key_pressed(self.moveLeftKeybind)):
            worldOffset[0] += self.moveLeft()

        if (self.keyboard.key_pressed(self.moveRightKeybind)):
            worldOffset[0] += self.moveRight()

        return worldOffset

    def moveUp(self):
        self.gameObject.y -= self.ySpeed * self.window.delta_time()
        if (self.gameObject.y < 128):
            self.gameObject.y = 128            
            return 32
        return 0

    def moveDown(self):
        self.gameObject.y += self.ySpeed * self.window.delta_time()
        if (self.gameObject.y > self.window.height - self.gameObject.height - 128):
            self.gameObject.y = self.window.height - self.gameObject.height - 128
            return -32
        return 0

    def moveLeft(self):
        self.gameObject.x -= self.xSpeed * self.window.delta_time()
        if (self.gameObject.x < 256):
            self.gameObject.x = 256
            return 32
        return 0            
    

    def moveRight(self):
        self.gameObject.x += self.xSpeed * self.window.delta_time()
        if (self.gameObject.x > self.window.width - self.gameObject.width - 256):
            self.gameObject.x = self.window.width - self.gameObject.width - 256
            return -32
        return 0            
