# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 19:58:59 2017

@author: anonymous
"""

import pygame
import constants
import levels
from player import Player

class Game(object):
    """ This class represents an instance of the game. If we need to reset
    the game we'd just need to create a new instance of this class """
    def __init__(self):
        # Create the player
        self.player = Player()
        
        # Create all the levels
        self.level_list = []
        self.level_list.append(levels.Level_01(player))
        self.level_list.append(levels.Level_02(player))
        
        # Set the current level
        self.current_level_no = 0
        self.current_level = level_list[current_level_no]
        
        active_sprite_list

def main():
    """ Main Program Function """
    # Initialize pygame
    pygame.init()
    
    # Set the window settings
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("CUNTRA")
    
    # Loop until the user clicks close button
    done = False
    
    # Used to limit FPS
    clock = pygame.time.Clock()
    
    # Create an instance of Game class
    game = Game()
    
    # ---------- MAIN PROGRAM LOOP ---------- #
    while not done:
        # Process events
        done = game.process_events()
        
        # Update object positions, check for collissions
        game.run_logic()
        
        # Draw the current frame
        game.display_frame(screen)
        
        # Limit FPS
        clock.tick(60)
        
    pygame.quit()
    
# Call the main function, start up the game
if __name__ == "__main__":
    main()