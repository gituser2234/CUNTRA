# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 20:26:13 2017

@author: anonymous
"""

import pygame
import constants

class Platform(pygame.sprite.Sprite):
    """ Platform that player can jump on """
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
        an array of 5 numbers like what's defined at the top of this code. """
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(constants.GREEN)
        
        self.rect = self.image.get_rect()