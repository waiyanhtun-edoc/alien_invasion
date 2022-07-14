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
        self._screen()
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for game"""
        while True:
            self._check_event()
            self._update_screen()

    def _check_event(self):
        """Check the event of keyboard keypress"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
    
    def _update_screen(self):
        """Update images on the screen,and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()
    
    def _screen(self):
        """initiize of screeen"""
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        self.caption = pygame.display.set_caption(self.settings.caption)
        self.icon = pygame.display.set_icon(self.settings.icon)


if __name__ == '__main__':
    #Make a game instance , run the game
    ai = AlienInvasion()
    ai.run_game()

