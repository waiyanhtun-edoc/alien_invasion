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

        #bullet Settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60 ,60 ,60)