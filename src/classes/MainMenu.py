import sys
import src.classes.Button
import src.classes.Game

class MainMenu:
    window = None
    mouse = None
    keyboard = None
    screen = None

    def __init__(self, window, mouse, keyboard):
        self.window = window
        self.mouse = mouse
        self.keyboard = keyboard
        self.screen = self

        self.title = src.pplay.sprite.Sprite("./assets/images/logo.png")

        self.playButton = src.classes.Button.Button("./assets/images/play_button.png", 0, 0)
        self.exitButton = src.classes.Button.Button("./assets/images/exit_button.png", 0, 0)

        self.title.x = (self.window.width / 2) - self.title.width / 2
        self.title.y = 50

        self.playButton.gameObject.x = (self.window.width / 2) - self.playButton.gameObject.width / 2
        self.playButton.gameObject.y = 200

        self.exitButton.gameObject.x = (self.window.width / 2) - self.exitButton.gameObject.width / 2
        self.exitButton.gameObject.y = 300

    def drawScreen(self):
        self.title.draw()
        self.playButton.gameObject.draw()
        self.exitButton.gameObject.draw()

    def loop(self, clicked):
        self.drawScreen()

        if (self.mouse.is_over_object(self.playButton.gameObject) and clicked):
            self.screen = src.classes.Game.Game(self.window, self.mouse, self.keyboard)

        if (self.mouse.is_over_object(self.exitButton.gameObject) and clicked):
            sys.exit()