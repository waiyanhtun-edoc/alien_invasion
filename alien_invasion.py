import sys

import pygame

class AlienInvasion:
    """Somethings"""
    def __init__(self):
        """Somethings"""
        pygame.init()

        self.screen = pygame.display.set_mode((1000,600))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Somethings"""
        while True:
            #Watch the keyboard and mouse event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
            
                pygame.display.flip()
            
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()