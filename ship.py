import imp
from turtle import Screen
import pygame

class Ship:
    """A class manage the ship"""

    def __init__(self,ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect() 

        #Load the ship image 
        self.image = pygame.image.load("images/ship.png")
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom of center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #movement flag
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw the ship at the current location"""
        self.screen.blit(self.image,self.rect)
    
    def update(self):
        """Update the ship position based on teh movement flag"""
        if self.moving_right:
            self.rect.x += 1
        elif self.moving_left:
            self.rect.x -= 1


        