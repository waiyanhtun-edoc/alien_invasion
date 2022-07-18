from asyncio import FastChildWatcher
from math import fabs
import sys
from tkinter.tix import Tree
from settings import Settings
from ship import Ship
import pygame
from bullets import Bullet

class AlienInvasion:
    """Over all class to mangage assets and behavior."""

    def __init__(self):
        """Initialize the game,and create game resource"""
        pygame.init()
        self.settings = Settings()
        self._screen()
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for game"""
        while True:
            self._check_event()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_event(self):
        """Check the event of keyboard keypress"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                self._check_keydown_events(event)
                self._check_keyup_events(event)
    
    def _check_keydown_events(self,event):
        """Check the keydown event"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()
    
    def _check_keyup_events(self,event):
        """Check the keydown event"""
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
    
    def _fire_bullet(self):
        """Sreate a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        """Update images on the screen,and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()
    
    def _screen(self):
        """initiize of screeen"""
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.caption = pygame.display.set_caption(self.settings.caption)
        self.icon = pygame.display.set_icon(self.settings.icon)

    def _update_bullets(self):
        """Update positio of bullets and get rid of old bullets."""
        #Update bullet positions.
        self.bullets.update()
        #Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


if __name__ == '__main__':
    #Make a game instance , run the game
    ai = AlienInvasion()
    ai.run_game()

