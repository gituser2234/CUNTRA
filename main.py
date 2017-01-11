# -*- coding: utf-8 -*-
"""

"""

import pygame
import constants
from player import Player
from rooms import Room1, Room2, Room3


class Game(object):
    """ This class represents an instance of the game. If we need to reset
    the game we'd just need to create a new instance of this class """
    def __init__(self):
        # Create all sprite list
        self.moving_sprite_list = pygame.sprite.Group()
        
        # Create the player
        self.player = Player(50, 50)
        self.moving_sprite_list.add(self.player) 
        
        # Create the rooms
        self.rooms = []
        
        room = Room1()
        self.rooms.append(room)
        
        room = Room2()
        self.rooms.append(room)
        
        room = Room3()
        self.rooms.append(room)
        
        self.current_room_no = 0
        self.current_room = self.rooms[self.current_room_no]
        
        
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
        self.player.move(self.current_room.wall_list)
        
        if self.player.rect.x < -15:
            if self.current_room_no == 0:
                self.current_room_no = 2
                self.current_room = self.rooms[self.current_room_no]
                self.player.rect.x = 790
            elif self.current_room_no == 2:
                self.current_room_no = 1
                self.current_room = self.rooms[self.current_room_no]
                self.player.rect.x = 790
            else:
                self.current_room_no = 0
                self.current_room = self.rooms[self.current_room_no]
                self.player.rect.x = 790
 
        if self.player.rect.x > 801:
            if self.current_room_no == 0:
                self.current_room_no = 1
                self.current_room = self.rooms[self.current_room_no]
                self.player.rect.x = 0
            elif self.current_room_no == 1:
                self.current_room_no = 2
                self.current_room = self.rooms[self.current_room_no]
                self.player.rect.x = 0
            else:
                self.current_room_no = 0
                self.current_room = self.rooms[self.current_room_no]
                self.player.rect.x = 0
        
        
        
    def display_frame(self, screen):
        """ Display everything to the screen of the game """
        screen.fill(constants.BLACK)
        
        self.moving_sprite_list.draw(screen)
        self.current_room.wall_list.draw(screen)
        
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
        