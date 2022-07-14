import pygame

class Settings:
    """A class all settings for alien_invasion"""

    def __init__(self):
        """Initialize the game settings"""

        #screen Settings
        self.bg_color = (148, 180, 159)
        self.caption =("ငါလိုးပိုင်ဂိမ်းဟ")
        self.icon = pygame.image.load("images/icon.png")
        self.ship_speed = 1.5