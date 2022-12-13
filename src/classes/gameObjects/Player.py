import pygame
from src.pplay.sprite import *
import src.classes.gameObjects.Weapon


class Player:
    absoluteSpeed = 200
    moveUpKeybind = "W"
    moveDownKeybind = "S"
    moveLeftKeybind = "A"
    moveRightKeybind = "D"
    throwWeaponKeybind = "SPACE"
    absoluteThrowCooldown = 0.5
    spacePressed = False

    def __init__(self, window, keyboard):
        self.window = window
        self.keyboard = keyboard
        self.gameObject = Sprite("./assets/images/player.png", 1)

        self.gameObject.x = (self.window.width / 2) - \
            (self.gameObject.width / 2)
        self.gameObject.y = (self.window.height / 2) - \
            (self.gameObject.height / 2)

        self.absoluteSpeed = self.absoluteSpeed
        self.xSpeed = self.absoluteSpeed
        self.ySpeed = self.absoluteSpeed

        self.weapon = src.classes.gameObjects.Weapon.Weapon(
            self.window, self.keyboard, self)
        self.hasWeapon = True

        self.throwCooldown = 0

    def control(self, mouseX, mouseY):
        self.absoluteSpeed = 200
        self.throwCooldown -= self.window.delta_time()
        if (self.throwCooldown < 0):
            self.throwCooldown = 0

        if (pygame.key.get_mods() & pygame.KMOD_SHIFT):
            self.absoluteSpeed = 400

        self.xSpeed = self.absoluteSpeed
        self.ySpeed = self.absoluteSpeed

        if (self.keyboard.key_pressed(self.moveUpKeybind)):
            self.moveUp()

        if (self.keyboard.key_pressed(self.moveDownKeybind)):
            self.moveDown()

        if (self.keyboard.key_pressed(self.moveLeftKeybind)):
            self.moveLeft()

        if (self.keyboard.key_pressed(self.moveRightKeybind)):
            self.moveRight()

        if (self.keyboard.key_pressed(self.throwWeaponKeybind) and self.throwCooldown == 0):
            self.throwCooldown = self.absoluteThrowCooldown

            if (self.hasWeapon):
                self.weapon.launch(mouseX, mouseY)
                self.hasWeapon = False
            else:
                self.weapon.returnToPlayer()
            self.spacePressed = False

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
