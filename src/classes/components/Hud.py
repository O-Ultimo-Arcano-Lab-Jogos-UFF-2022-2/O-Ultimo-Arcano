import pygame
from src.pplay.sprite import *


class HUD:
    hpColor = (200, 0, 0)
    staminaColor = (0, 180, 0)

    def __init__(self, window, player, waveManager):
        self.window = window
        self.player = player
        self.waveManager = waveManager

    def draw(self):
        hpBarMaxWidth = 2 * self.player.maxHp
        hpBarCurrentWidth = hpBarMaxWidth * \
            (self.player.currentHp / self.player.maxHp)

        staminaBarMaxWidth = 100 * self.player.absoluteSprintStamina
        staminaBarCurrentWidth = staminaBarMaxWidth * \
            (self.player.sprintStamina / self.player.absoluteSprintStamina)

        # HP Bar
        pygame.draw.rect(self.window.screen, (0, 0, 0),
                         pygame.Rect(30, 30, hpBarMaxWidth, 20), 0, 4)
        pygame.draw.rect(self.window.screen, self.hpColor,
                         pygame.Rect(30, 30, hpBarCurrentWidth, 20), 0, 4)

        # Stamina Bar
        pygame.draw.rect(self.window.screen, (0, 0, 0),
                         pygame.Rect(30, 60, staminaBarMaxWidth, 20), 0, 4)
        pygame.draw.rect(self.window.screen, self.staminaColor,
                         pygame.Rect(30, 60, staminaBarCurrentWidth, 20), 0, 4)
