from curses import window
from turtle import width
import src.classes.scenes.MainMenu
import src.classes.gameObjects.Player
from pytmx.util_pygame import load_pygame

class Game:
    window = None
    mouse = None
    keyboard = None
    screen = None
    player = None
    tmxdata = None
    worldOffset = [-1024, -1024]

    def __init__(self, window, mouse, keyboard):
        self.window = window
        self.mouse = mouse
        self.keyboard = keyboard
        self.screen = self
        self.player = src.classes.gameObjects.Player.Player(window, keyboard)
        self.tmxdata = load_pygame("./assets/maps/SnowMap.tmx")

    def blitAllTiles(self):
        for layer in self.tmxdata:
            for tile in layer.tiles():
                xPixel = tile[0] * 32 + self.worldOffset[0]
                yPixel = tile[1] * 32 + self.worldOffset[1]
                self.window.screen.blit(tile[2], (xPixel, yPixel))

        self.player.gameObject.draw()

    def drawScreen(self):
        self.blitAllTiles()

    def loop(self, click):
        self.drawScreen()

        self.worldOffset = self.player.control(self.worldOffset)

        if (self.keyboard.key_pressed("ESC")):
            self.screen = src.classesclasses.scenes.MainMenu.MainMenu(self.window, self.mouse, self.keyboard)
