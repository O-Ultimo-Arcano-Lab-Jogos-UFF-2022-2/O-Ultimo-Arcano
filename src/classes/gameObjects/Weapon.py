import math
from src.pplay.sprite import *

class Weapon:
	absoluteSpeed = 400
	weaponRange = 500
	direction = None

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

	def launch(self, direction):
		self.gameObject.x = self.player.gameObject.x
		self.gameObject.y = self.player.gameObject.y
		self.launchPointX = self.gameObject.x
		self.launchPointY = self.gameObject.y

		self.visible = True
		self.flying = True
		self.direction = direction

	def returnToPlayer(self):
		self.flying = False
		self.returning = True

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
			if ("N" in self.direction):
				self.moveUp()

			if ("E" in self.direction):
				self.moveRight()

			if ("S" in self.direction):
				self.moveDown()

			if ("W" in self.direction):
				self.moveLeft()
	
	def returningToPlayer(self):
		if (self.returning):
			if (self.gameObject.collided(self.player.gameObject)):
				self.returning = False
				self.visible = False
				self.player.hasWeapon = True

			if (self.gameObject.x > self.player.gameObject.x):
				self.gameObject.x -= self.xSpeed * self.window.delta_time()

			elif (self.gameObject.x < self.player.gameObject.x):
				self.gameObject.x += self.xSpeed * self.window.delta_time()

			if (self.gameObject.y > self.player.gameObject.y):
				self.gameObject.y -= self.ySpeed * self.window.delta_time()

			elif (self.gameObject.y < self.player.gameObject.y):
				self.gameObject.y += self.ySpeed * self.window.delta_time()

	def moveUp(self):
		self.gameObject.y -= self.ySpeed * self.window.delta_time()
		if (self.gameObject.y < 0):
				self.gameObject.y = 0
				self.flying = False

	def moveDown(self):
		self.gameObject.y += self.ySpeed * self.window.delta_time()
		if ((self.gameObject.y + self.gameObject.height) > self.window.height):
			self.gameObject.y = self.window.height - self.gameObject.height
			self.flying = False

	def moveLeft(self):
		self.gameObject.x -= self.xSpeed * self.window.delta_time()
		if (self.gameObject.x < 0):
				self.gameObject.x = 0
				self.flying = False

	def moveRight(self):
		self.gameObject.x += self.xSpeed * self.window.delta_time()
		if (self.gameObject.x > self.window.width - self.gameObject.width):
			self.gameObject.x = self.window.width - self.gameObject.width
			self.flying = False

	def control(self):
		if (self.gameObject.collided(self.player.gameObject) and not self.player.hasWeapon and not self.flying):
			self.catch()

		if (self.player.weapon.flying):
			self.player.weapon.fly()
		
		elif (self.player.weapon.returning):
			self.player.weapon.returningToPlayer()