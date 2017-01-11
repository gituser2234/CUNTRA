# -*- coding: utf-8 -*-
"""

"""

import pygame
import constants

class Player(pygame.sprite.Sprite):
    """ This class represents a player """
    def __init__(self, x, y):
        # Call parent's class constructor
        super().__init__()
        
        # Set details
        self.image = pygame.Surface([20, 20])
        self.image.fill(constants.RED)
        
        # Make our top-left corner the passed-in location
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # --- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        
    def changespeed(self, x, y):
        """ Change the speed of the player """
        self.change_x += x
        self.change_y += y
        
    def update(self, walls):
        """ Find a new position for the player """
        # Move left/right
        self.rect.x += self.change_x
        
        # Did this update causes us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # Set our right side to the edge of the block
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
                
        # Move up/down
        self.rect.y += self.change_y
        
        # Did this update causes us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
                    
        
        