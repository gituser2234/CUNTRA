# -*- coding: utf-8 -*-
"""

"""

import pygame
import constants

class Wall(pygame.sprite.Sprite):
    """ A wall the player can't run through """
    def __init__(self, x, y, width, height):
        super().__init__()
        
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(constants.BLUE)
        
        # Make our top-left corner the passed-in location
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y