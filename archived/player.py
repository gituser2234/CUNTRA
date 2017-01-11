# -*- coding: utf-8 -*-
"""

"""

import pygame
import constants

class Player(pygame.sprite.Sprite):
    """ This class represents a player """
    
    # List of sprites we can bump against
    level = None
    
    def __init__(self, x, y):
        # Call parent's class constructor
        super().__init__()
        
        # Set details
        self.image = pygame.Surface([40, 60])
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
        # Gravity
        self.calc_grav()
        
        # Move left/right
        self.rect.x += self.change_x
        pos = self.rect.x
        
        # Did this update causes us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
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
        
    def jump(self):
        """ Called when user hits 'jump' key """
        # Move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
        
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -10
            
    # Player controlled movement
    def go_left(self):
        self.change_x = -6
    
    def go_right(self):
        self.change_x = 6
        
    def stop(self):
        self.change_x = 0
        
    def calc_grav(self):
        """ Calculate effect of gravity """
        if self.change_y == 0:
            self.change_y == 1
        else:
            self.change_y += .35
            
        # See if we are on the ground
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height