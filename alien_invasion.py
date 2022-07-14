import sys
from settings import Settings
from ship import Ship
import pygame

class AlienInvasion:
    """Over all class to mangage assets and behavior."""

    def __init__(self):
        """Initialize the game,and create game resource"""
        pygame.init()
        self.settings = Settings()
        #set the screen size and set the caption
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("ငါလိုးပိုင်ဂိမ်းဟ")
        self.ship = Ship(self)


    def run_game(self):
        """Start the main loop for game"""
        while True:

            #background color
            self.screen.fill(self.settings.bg_color)

            #player ship show
            self.ship.blitme()

            #Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance , run the game
    ai = AlienInvasion()
    ai.run_game()

