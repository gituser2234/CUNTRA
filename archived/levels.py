# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 19:49:24 2017

@author: anonymous
"""
import pygame
from constants import BLUE

class Level():
    platform_list = None
    enemy_list = None
    
    # Background image
    background = None
    
    def __init__(self, player):
        """ Constructor. Pass in a handle to player.
        Needed for when moving platforms collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
        
    # Update everything
    def update(self):
        self.platform_list.update()
        self.enemy_list.update()
        
    # Draw everything on the screen
    def draw(self, screen):
        screen.fill(BLUE)
        
        self.platform_list.draw()
        self.enemy_list.draw()
        
class Level1(Level):
    def __init__(self, player):
        super().__init__()
        
        # Array with width, height, x, and y of platform
        self.level = [ [210, 70, 500, 500],
                       [210, 70, 200, 400],
                       [210, 70, 600, 300], ]
                       
        