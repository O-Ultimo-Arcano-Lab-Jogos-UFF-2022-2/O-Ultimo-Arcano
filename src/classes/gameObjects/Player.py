from src.pplay.sprite import *

class Player:
    absoluteSpeed = 400
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

    def control(self):
        if (self.keyboard.key_pressed(self.moveUpKeybind)):
            self.moveUp()

        if (self.keyboard.key_pressed(self.moveDownKeybind)):
            self.moveDown()

        if (self.keyboard.key_pressed(self.moveLeftKeybind)):
            self.moveLeft()

        if (self.keyboard.key_pressed(self.moveRightKeybind)):
            self.moveRight()

    def moveUp(self):
        self.gameObject.y -= self.ySpeed * self.window.delta_time()
        if (self.gameObject.y < 0):
            self.gameObject.y = 0

    def moveDown(self):
        self.gameObject.y += self.ySpeed * self.window.delta_time()
        if ((self.gameObject.y + self.gameObject.height) > self.window.height):
            self.gameObject.y = self.window.height - self.gameObject.height

    def moveLeft(self):
        self.gameObject.x -= self.xSpeed * self.window.delta_time()
        if (self.gameObject.x < 0):
            self.gameObject.x = 0

    def moveRight(self):
        self.gameObject.x += self.xSpeed * self.window.delta_time()
        if (self.gameObject.x > self.window.width - self.gameObject.width):
            self.gameObject.x = self.window.width - self.gameObject.width