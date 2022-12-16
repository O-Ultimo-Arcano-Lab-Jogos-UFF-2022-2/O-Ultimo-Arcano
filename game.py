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

# Game Over Flags Initialization
gameWindow.gameOver = False
gameWindow.playerHasWon = False

# Controls Initialization
keyboard = gameWindow.get_keyboard()
mouse = gameWindow.get_mouse()
leftButtonPreviousStatus = False
scrollButtonPreviousStatus = False
rightButtonPreviousStatus = False

# Initialize Screen
currentScreen = src.classes.scenes.MainMenu.MainMenu(
    gameWindow, mouse, keyboard)

# Game Loop
while (gameWindow):
    # Events Loop
    [leftButtonCurrentStatus, scrollButtonCurrentStatus,
        rightButtonCurrentStatus] = pygame.mouse.get_pressed()

    # Current Screen Game Loop
    leftClick = leftButtonCurrentStatus and not leftButtonPreviousStatus
    scrollClick = scrollButtonCurrentStatus and not scrollButtonPreviousStatus
    rightClick = rightButtonCurrentStatus and not rightButtonPreviousStatus

    currentScreen.loop(leftClick, rightClick)

    leftButtonPreviousStatus = leftButtonCurrentStatus
    scrollButtonPreviousStatus = scrollButtonCurrentStatus
    rightButtonPreviousStatus = rightButtonCurrentStatus

    # Get Next Screen
    currentScreen = currentScreen.screen

    # Update Window
    gameWindow.update()
    clock.tick(60)
