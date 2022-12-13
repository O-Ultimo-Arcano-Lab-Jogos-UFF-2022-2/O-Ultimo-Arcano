# Imports
import sys
import pygame
from screeninfo import get_monitors
from pygame.locals import *
from src.pplay.window import *
import src.classes.scenes.MainMenu

# Initializes pygame's modules
pygame.init()
clock = pygame.time.Clock()

# Get Primary Monitor


def get_primary_monitor():
    for monitor in get_monitors():
        if monitor.is_primary:
            return monitor

    return None


# Game Window Initialization
primaryMonitor = get_primary_monitor()
# gameWindow = Window(primaryMonitor.width, primaryMonitor.height)
gameWindow = Window(1216, 800)
gameWindow.set_title("O Ultimo Arcano")
gameWindow.clock = clock

# Controls Initialization
keyboard = gameWindow.get_keyboard()
mouse = gameWindow.get_mouse()
leftClick = False
rightClick = False

# Initialize Screen
currentScreen = src.classes.scenes.MainMenu.MainMenu(
    gameWindow, mouse, keyboard)

# Game Loop
while (gameWindow):
    # Resets variable that sees if mouse is right clicking
    leftClick = False
    rightClick = False

    # Events Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                leftClick = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                leftClick = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                rightClick = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3:
                rightClick = False

    # Current Screen Game Loop
    currentScreen.loop(leftClick, rightClick)

    # Get Next Screen
    currentScreen = currentScreen.screen

    # Update Window
    gameWindow.update()
    clock.tick(60)
