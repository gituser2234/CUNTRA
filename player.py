# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 20:09:42 2017

@author: anonymous
"""

import pygame
import constants

class Player(pygame.sprite.Sprite):
    def __init__(self):
        # Call parent's constructor
        super().__init__()
        
        # Create an image and set a referance to this object
        self.image = pygame.image.load("kzk.jpg").convert()
        self.rect = self.image.get_rect()
        
        # Set the speed vector
        self.change_x = 0
        self.change_y = 0
        
        # List of sprites we can bump against
        self.level = None
    
    def update(self):
        """ Move the player """
        # Gravity
        self.calc_grav()
        
        # Move left/right
        self.rect.x += self.change_x
        
        # See if we hit something
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we hit something set our positions to the edge
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right
                
        # Move up/down
        self.rect.y += self.change_y
        
        # Another check if we hit something
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we hit something set our positions to the edge
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom   
            
            # Stop our vertical movement
            self.change_y = 0
            
    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
            
        # See if we are on the ground
        if self.rect.y + self.rect.height >= constants.SCREEN_HEIGHT and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height
            
    def jump(self):
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
        
        # If it is okay to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -10
            
    # Player controlled movement
    def go_left(self):
        self.change_x = -6
        
    def go_right(self):
        self.change_x = 6
        
    def stop(self):
        self.change_x = 0