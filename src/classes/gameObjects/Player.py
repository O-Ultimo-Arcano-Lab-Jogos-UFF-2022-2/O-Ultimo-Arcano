import pygame
import src.classes.gameObjects.Weapon
from src.classes.utils.Vector import Vector
from src.pplay.sprite import *
from src.classes.utils.ObjectRect import ObjectRect


class Player:
    absoluteSpeed = 200
    moveUpKeybind = "W"
    moveDownKeybind = "S"
    moveLeftKeybind = "A"
    moveRightKeybind = "D"
    absoluteThrowCooldown = 0.5
    absoluteInvincibilityCooldown = 1
    absoluteSprintStamina = 2
    maxHp = 100

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

        self.currentHp = self.maxHp
        self.invincibilityCooldown = 0

        self.sprintStamina = self.absoluteSprintStamina
        self.rechargingStamina = False

    def control(self, leftClick, rightClick, mouseLocation):
        # Reseting player speed while not sprinting
        self.absoluteSpeed = 200

        # Recharging Throw Weapon Cooldown
        if (self.throwCooldown != 0):
            self.throwCooldown = max(
                self.throwCooldown - self.window.delta_time(), 0)

        # Counting Invincibility Frames
        if (self.invincibilityCooldown != 0):
            self.invincibilityCooldown = max(
                self.invincibilityCooldown - self.window.delta_time(), 0)

        # Recharging Stamina
        if self.rechargingStamina and self.sprintStamina < self.absoluteSprintStamina:
            self.sprintStamina = min(
                self.sprintStamina + self.window.delta_time(), self.absoluteSprintStamina)
        if self.rechargingStamina and self.sprintStamina == self.absoluteSprintStamina:
            self.rechargingStamina = False

        # Sprint Controls
        if not self.rechargingStamina:
            if (pygame.key.get_mods() & pygame.KMOD_SHIFT and self.sprintStamina > 0):
                self.absoluteSpeed = 400
                self.sprintStamina = max(
                    self.sprintStamina - self.window.delta_time(), 0)
            else:
                self.sprintStamina = min(
                    self.sprintStamina + self.window.delta_time(), self.absoluteSprintStamina)

        # Set Sprint to Recharge Mode if player has exhausted the stamina
        if self.sprintStamina == 0:
            self.rechargingStamina = True

        self.xSpeed = self.absoluteSpeed
        self.ySpeed = self.absoluteSpeed

        # Player Movement
        if (self.keyboard.key_pressed(self.moveUpKeybind)):
            self.moveUp()

        if (self.keyboard.key_pressed(self.moveDownKeybind)):
            self.moveDown()

        if (self.keyboard.key_pressed(self.moveLeftKeybind)):
            self.moveLeft()

        if (self.keyboard.key_pressed(self.moveRightKeybind)):
            self.moveRight()

        # Throw Weapon
        if (leftClick and self.hasWeapon):
            self.throwCooldown = self.absoluteThrowCooldown
            self.weapon.launch(mouseLocation)
            self.hasWeapon = False

        if (rightClick and not self.hasWeapon):
            self.weapon.returnToPlayer()

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

    def takeHit(self, damage):
        if (self.invincibilityCooldown == 0):
            self.currentHp = max(self.currentHp - damage, 0)

            if self.currentHp == 0:
                self.window.gameOver = True
                self.window.playerHasWon = False

    def getRect(self):
        return ObjectRect(self.gameObject)
