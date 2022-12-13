import math
from src.pplay.sprite import *


class Weapon:
    absoluteSpeed = 450
    weaponRange = 600

    def __init__(self, window, keyboard, player):
        self.window = window
        self.keyboard = keyboard
        self.gameObject = Sprite("./assets/images/weapon.png", 1)
        self.player = player

        self.absoluteSpeed = self.absoluteSpeed
        self.xSpeed = self.absoluteSpeed
        self.ySpeed = self.absoluteSpeed

        self.distanceFromLaunchPoint = self.weaponRange
        self.flying = False
        self.returning = False
        self.visible = False

    def launch(self, mouseX, mouseY):
        self.gameObject.x = self.player.gameObject.x
        self.gameObject.y = self.player.gameObject.y
        self.launchPointX = self.gameObject.x
        self.launchPointY = self.gameObject.y

        self.visible = True
        self.flying = True

        self.mouseX = mouseX
        self.mouseY = mouseY

    def returnToPlayer(self):
        self.flying = False
        self.returning = True
        self.launchPointY = self.gameObject.y
        self.launchPointX = self.gameObject.x

    def catch(self):
        self.flying = False
        self.returning = False
        self.visible = False
        self.player.hasWeapon = True

    def calculateDistanceFromLaunch(self):
        playerX = self.player.gameObject.x
        playerY = self.player.gameObject.y
        weaponX = self.gameObject.x
        weaponY = self.gameObject.y

        return math.sqrt(pow(playerX - weaponX, 2) + pow(playerY - weaponY, 2))

    def fly(self):
        self.distanceFromLaunchPoint = self.calculateDistanceFromLaunch()

        if (self.distanceFromLaunchPoint >= self.weaponRange):
            self.flying = False

        if (self.flying):
            self.moveX(self.mouseX)
            self.moveY(self.mouseY)

    def returningToPlayer(self):
        if (self.returning):
            if (self.gameObject.collided(self.player.gameObject)):
                self.returning = False
                self.visible = False
                self.player.hasWeapon = True

            self.moveX(self.player.gameObject.x)
            self.moveY(self.player.gameObject.y)

    def moveY(self, destination):
        self.gameObject.y += (destination - self.launchPointY) * \
            self.window.delta_time()

        if (self.gameObject.y < 0):
            self.gameObject.y = 0
            self.flying = False
            self.returning = False

        if ((self.gameObject.y + self.gameObject.height) > self.window.height):
            self.gameObject.y = self.window.height - self.gameObject.height
            self.flying = False
            self.returning = False

    def moveX(self, destination):
        self.gameObject.x += (destination - self.launchPointX) * \
            self.window.delta_time()

        if (self.gameObject.x < 0):
            self.gameObject.x = 0
            self.flying = False
            self.returning = False

        if (self.gameObject.x > self.window.width - self.gameObject.width):
            self.gameObject.x = self.window.width - self.gameObject.width
            self.flying = False
            self.returning = False

    def control(self):
        if (self.gameObject.collided(self.player.gameObject) and not self.player.hasWeapon and not self.flying):
            self.catch()

        if (self.flying):
            self.fly()

        elif (self.returning):
            self.returningToPlayer()
