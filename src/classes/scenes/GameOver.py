import pygame
import src.classes.scenes.MainMenu


class GameOver:
    absoluteReturnCooldown = 3
    background = pygame.image.load("./assets/images/background.png")

    def __init__(self, window, mouse, keyboard):
        self.window = window

        self.mouse = mouse
        self.keyboard = keyboard
        self.screen = self

        if (self.window.playerHasWon):
            self.title = src.pplay.sprite.Sprite(
                "./assets/images/game_over_victory.png")
        else:
            self.title = src.pplay.sprite.Sprite(
                "./assets/images/game_over_defeat.png")

        self.title.x = (self.window.width / 2) - self.title.width / 2
        self.title.y = (self.window.height / 2) - self.title.height / 2

        self.returnCooldown = self.absoluteReturnCooldown

    def drawScreen(self):
        self.window.screen.blit(self.background, (0, 0))
        self.title.draw()

    def loop(self, leftClick, rightClick):
        if (self.returnCooldown != 0):
            self.returnCooldown = max(
                self.returnCooldown - self.window.delta_time(), 0)

        # Reset Game Over
        self.window.gameOver = False
        self.window.playerHasWon = False

        self.drawScreen()

        if (self.returnCooldown == 0):
            self.screen = src.classes.scenes.MainMenu.MainMenu(
                self.window, self.mouse, self.keyboard)
