import math
from src.classes.utils.Vector import Vector
from src.pplay.sprite import *


class Weapon:
    absoluteSpeed = Vector(450, 450)
    weaponRange = 600

    def __init__(self, window, keyboard, player):
        self.window = window
        self.keyboard = keyboard
        self.gameObject = Sprite("./assets/images/weapon.png", 1)
        self.player = player

        self.speed = Vector(0, 0)

        self.distanceFromLaunchPoint = self.weaponRange
        self.flying = False
        self.returning = False
        self.visible = False

    def launch(self, mouseLocation):
        self.gameObject.x = self.player.gameObject.x
        self.gameObject.y = self.player.gameObject.y
        self.launchPoint = Vector(
            self.gameObject.x, self.gameObject.y)

        self.visible = True
        self.flying = True

        self.mouseLocation = mouseLocation

    def returnToPlayer(self):
        self.flying = False
        self.returning = True
        self.launchPoint = Vector(
            self.gameObject.x, self.gameObject.y)

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
            self.move(self.mouseLocation)

    def returningToPlayer(self):
        if (self.returning):
            if (self.gameObject.collided(self.player.gameObject)):
                self.returning = False
                self.visible = False
                self.player.hasWeapon = True

            playerLocation = Vector(
                self.player.gameObject.x, self.player.gameObject.y)
            self.move(playerLocation)

    def move(self, destination):
        direction = Vector.fromObjects(
            self.launchPoint, destination).unit()
        self.speed = self.absoluteSpeed.copyDirection(direction)

        self.gameObject.x += self.speed.x * self.window.delta_time()
        self.gameObject.y += self.speed.y * self.window.delta_time()

        if (self.gameObject.x < 0):
            self.gameObject.x = 0
            self.flying = False
            self.returning = False

        if (self.gameObject.x > self.window.width - self.gameObject.width):
            self.gameObject.x = self.window.width - self.gameObject.width
            self.flying = False
            self.returning = False

        if (self.gameObject.y < 0):
            self.gameObject.y = 0
            self.flying = False
            self.returning = False

        if ((self.gameObject.y + self.gameObject.height) > self.window.height):
            self.gameObject.y = self.window.height - self.gameObject.height
            self.flying = False
            self.returning = False

    def control(self):
        if (self.gameObject.collided(self.player.gameObject) and not self.player.hasWeapon and not self.flying):
            self.catch()

        if (self.flying):
            self.fly()

        elif (self.returning):
            self.returningToPlayer()
