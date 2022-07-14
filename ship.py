import imp
from turtle import Screen
import pygame

class Ship:
    """A class manage the ship"""

    def __init__(self,ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings =  ai_game.settings
        self.screen_rect = ai_game.screen.get_rect() 

        #Load the ship image 
        self.image = pygame.image.load("images/ship.png")
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom of center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x) 
        #movement flag
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw the ship at the current location"""
        self.screen.blit(self.image,self.rect)
    
    def update(self):
        """Update the ship position based on teh movement flag"""
        #update the ship's x value ,not rect
        if self.moving_right:
            self.x += self.settings.ship_speed
        elif self.moving_left:
            self.x -= self.settings.ship_speed
        
        #update the rect object from self.x
        self.rect.x = self.x


        