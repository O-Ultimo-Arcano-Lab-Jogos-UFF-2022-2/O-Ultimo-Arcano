import sys
import pygame
import src.classes.components.Button
import src.classes.scenes.Game


class MainMenu:
    background = pygame.image.load("./assets/images/background.png")

    def __init__(self, window, mouse, keyboard):
        self.window = window

        self.mouse = mouse
        self.keyboard = keyboard
        self.screen = self

        self.title = src.pplay.sprite.Sprite("./assets/images/logo.png")

        self.playButton = src.classes.components.Button.Button(
            "./assets/images/play_button.png", 0, 0)
        self.exitButton = src.classes.components.Button.Button(
            "./assets/images/exit_button.png", 0, 0)

        self.title.x = (self.window.width / 2) - self.title.width / 2
        self.title.y = 50

        self.playButton.gameObject.x = (
            self.window.width / 2) - self.playButton.gameObject.width / 2
        self.playButton.gameObject.y = 200

        self.exitButton.gameObject.x = (
            self.window.width / 2) - self.exitButton.gameObject.width / 2
        self.exitButton.gameObject.y = 300

    def drawScreen(self):
        self.window.screen.blit(self.background, (0, 0))
        self.title.draw()
        self.playButton.gameObject.draw()
        self.exitButton.gameObject.draw()

    def loop(self, leftClick, rightClick):
        # Reset Game Over
        self.window.gameOver = False
        self.window.playerHasWon = False

        self.drawScreen()

        if (self.mouse.is_over_object(self.playButton.gameObject) and leftClick):
            self.screen = src.classes.scenes.Game.Game(
                self.window, self.mouse, self.keyboard)

        if (self.mouse.is_over_object(self.exitButton.gameObject) and leftClick):
            sys.exit()
