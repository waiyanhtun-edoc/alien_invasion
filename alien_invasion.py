from ast import While
from platform import python_branch
import sys
from tkinter import W
from turtle import screensize

import pygame

class AlienInvasion:
    """Over all class to mangage assets and behavior."""

    def __init__(self):
        """Initialize the game,and create game resource"""
        pygame.init()

        #set the screen size and set the caption
        self.screen = pygame.display.set_mode((1000,600))
        pygame.display.set_caption("ငါလိုးပိုင်ဂိမ်းဟ")

        #setbackground color
        self.bg_color = (172, 125, 136)

    def run_game(self):
        """Start the main loop for game"""
        while True:

            #background color
            self.screen.fill((self.bg_color))

            #Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == "__main__":
    #Make a game instance , run the game
    ai = AlienInvasion()

    ai.run_game()

