import pygame
import src.classes.scenes.MainMenu
import src.classes.gameObjects.Player
import src.classes.components.HUD
from src.classes.gameObjects.WaveManager import WaveManager
from src.classes.gameObjects.Wave import Wave
from src.classes.gameObjects.enemies.Goblin import Goblin
from src.classes.gameObjects.enemies.Spider import Spider
from src.classes.gameObjects.HitboxManager import HitboxManager
class Game:
    background = pygame.image.load("./assets/maps/SnowMap.png")

    def __init__(self, window, mouse, keyboard):
        self.window = window
        self.mouse = mouse
        self.keyboard = keyboard
        self.screen = self
        self.player = src.classes.gameObjects.Player.Player(window, keyboard)

        # Waves de teste
        # @TODO Configurar as waves
        self.waveManager = WaveManager(window, [
            Wave(self, window, 1, [Spider, Spider]),  
        ])

        self.hud = src.classes.components.HUD.HUD(
            window, self.player, self.waveManager)

    def drawScreen(self):
        self.window.screen.blit(self.background, (0, 0))
        self.player.gameObject.draw()
        self.waveManager.draw()
        HitboxManager.draw()

        if (self.player.weapon.visible):
            self.player.weapon.gameObject.draw()

        self.hud.draw()

    def loop(self, leftClick, rightClick):
        mousePosition = self.mouse.get_position()
        self.player.control(mousePosition[0], mousePosition[1])
        self.player.weapon.control()
        self.waveManager.loop()
        HitboxManager.loop()

        self.drawScreen()
        
        if (self.keyboard.key_pressed("ESC")):
            self.screen = src.classes.scenes.MainMenu.MainMenu(
                self.window, self.mouse, self.keyboard)
