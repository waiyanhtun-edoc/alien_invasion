import sys

import pygame

from settings import Settings as set

class AlienInvasion:
    """Somethings"""
    def __init__(self):
        """Somethings"""
        pygame.init()
        self.settings = set()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        

    def run_game(self):
        """Somethings"""
        while True:
            #Watch the keyboard and mouse event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                #Redraw the screen during eash pass through the loop
                self.screen.fill(self.settings.bg_color)
            
                pygame.display.flip()
            
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()