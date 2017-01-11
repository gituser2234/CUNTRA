# -*- coding: utf-8 -*-
"""

"""

import pygame
import constants
from player import Player
from wall import Wall


class Game(object):
    """ This class represents an instance of the game. If we need to reset
    the game we'd just need to create a new instance of this class """
    def __init__(self):
        # Create all sprite list
        self.all_sprite_list = pygame.sprite.Group()
        
        # Create the player
        self.player = Player(50, 50)
        self.all_sprite_list.add(self.player) 
        
        # Make the walls
        self.wall_list = pygame.sprite.Group()
        
        wall = Wall(0, 0, 10, 600)
        self.wall_list.add(wall)
        self.all_sprite_list.add(wall)
        
        wall = Wall(10, 0, 730, 10)
        self.wall_list.add(wall)
        self.all_sprite_list.add(wall)
        
        wall = Wall(10, 200, 100, 10)
        self.wall_list.add(wall)
        self.all_sprite_list.add(wall)
        
        
    def process_events(self):
        """ Process all of the events. 
        Return True if we need to close the window. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
                
            # Set the speed based on key pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(-3, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.changespeed(3, 0)
                elif event.key == pygame.K_UP:
                    self.player.changespeed(0, -3)
                elif event.key == pygame.K_DOWN:
                    self.player.changespeed(0, 3)
                    
            # Reset speed then key goes up
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(3, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.changespeed(-3, 0)
                elif event.key == pygame.K_UP:
                    self.player.changespeed(0, 3)
                elif event.key == pygame.K_DOWN:
                    self.player.changespeed(0, -3)
                
        return False
        
    def run_logic(self):
        """ This method is run each time through the frame.
        It updates positions and checks for collissions. """
        self.player.update(self.wall_list)
        
        
    def display_frame(self, screen):
        """ Display everything to the screen of the game """
        screen.fill(constants.WHITE)
        
        self.all_sprite_list.draw(screen)
        
        pygame.display.flip()
        

def main():
    """ Main Program Function """
    # Initialize pygame
    pygame.init()
    
    # Set the window and its settings
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    
    pygame.display.set_caption("CUNTRA")
    #pygame.mouse.set_visible(False)
    
    # Loop until the user clicks close button
    done = False
    
    # Used to manage how fast screen updates
    clock = pygame.time.Clock()
    
    # Create an instance of the Game class
    game = Game()
    
    # ---------- MAIN PROGRAM LOOP ---------- #
    while not done:
        # Process events
        done = game.process_events()
        
        # Update object positions, check for collisions
        game.run_logic()
        
        # Draw the current frame
        game.display_frame(screen)
        
        # Limit FPS
        clock.tick(60)
        
    pygame.quit()
    
    
# Call the main function, start up the game
if __name__ == '__main__':
    main()
        