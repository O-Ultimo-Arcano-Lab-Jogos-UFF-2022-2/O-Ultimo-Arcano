import pygame
import src.classes.scenes.MainMenu
import src.classes.gameObjects.Player

class Game:
    background = pygame.image.load("./assets/maps/SnowMap.png")

    def __init__(self, window, mouse, keyboard):
        self.window = window
        self.mouse = mouse
        self.keyboard = keyboard
        self.screen = self
        self.player = src.classes.gameObjects.Player.Player(window, keyboard)

    def drawScreen(self):
        self.window.screen.blit(self.background, (0, 0))
        self.player.gameObject.draw()
        
        if (self.player.weapon.visible):
            self.player.weapon.gameObject.draw()

    def loop(self, click):
        self.player.control()
        self.player.weapon.control()

        self.drawScreen()

        if (self.keyboard.key_pressed("ESC")):
            self.screen = src.classes.scenes.MainMenu.MainMenu(self.window, self.mouse, self.keyboard)
