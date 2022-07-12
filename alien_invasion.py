import sys

import pygame

class AlienInvasion:
    """Somethings"""
    def __init__(self):
        """Somethings"""
        pygame.init()

        self.screen = pygame.display.set_mode((1000,600))
        pygame.display.set_caption("Alien Invasion")

        #set the background color
        self.bg_color = (250,200,255)

    def run_game(self):
        """Somethings"""
        while True:
            #Watch the keyboard and mouse event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                #Redraw the screen during eash pass through the loop
                self.screen.fill(self.bg_color)
            
                pygame.display.flip()
            
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()