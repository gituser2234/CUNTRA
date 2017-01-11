# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 19:58:59 2017

@author: anonymous
"""

import pygame
import constants
import levels
from player import Player


#class Game(object):
#    """ This class represents an instance of the game. If we need to reset
#    the game we'd just need to create a new instance of this class """
#    def __init__(self):
#        # Create the player
#        self.player = Player()
#        
#        # Create all the levels
#        self.level_list = []
#        self.level_list.append(levels.Level_01(self.player))
#        self.level_list.append(levels.Level_02(self.player))
#        
#        # Set the current level
#        self.current_level_no = 0
#        self.current_level = self.level_list[self.current_level_no]
#        
#        self.active_sprite_list = pygame.sprite.Group()
#        self.player.level = self.current_level
#        
#        self.player.rect.x = 340
#        self.player.rect.y = constants.SCREEN_HEIGHT - self.player.rect.height
#        self.active_sprite_list.add(self.player)
#        
#    def process_events(self):
#       for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                return True
# 
#            if event.type == pygame.KEYDOWN:
#                if event.key == pygame.K_LEFT:
#                    self.player.go_left()
#                if event.key == pygame.K_RIGHT:
#                    self.player.go_right()
#                if event.key == pygame.K_UP:
#                    self.player.jump()
# 
#            if event.type == pygame.KEYUP:
#                if event.key == pygame.K_LEFT and self.player.change_x < 0:
#                    self.player.stop()
#                if event.key == pygame.K_RIGHT and self.player.change_x > 0:
#                    self.player.stop()
#       return False
#                    
#    def run_logic(self):
#        """ This method is run each time through the frame.
#        It updates positions and checks for collisions. """
#        # Update the player
#        self.active_sprite_list.update()
#        
#        # Update items in the level
#        self.current_level.update()
#        
#        # If the player gets near the right side, shift the world (-x)
#        if self.player.rect.right >= 500:
#            diff = self.player.rect.right - 500
#            self.player.rect.right = 500
#            self.current_level.shift_world(-diff)
#        
#        # If the player gets near the left side, shift the world right (+x)
#        if self.player.rect.left <= 120:
#            diff = 120 - self.player.rect.left
#            self.player.rect.left = 120
#            self.current_level.shift_world(diff)
#            
#        # If the player gets to the end of the level, go to the next level
#        self.current_position = self.player.rect.x + self.current_level.world_shift
#        if self.current_position < self.current_level.level_limit:
#            self.player.rect.x = 120
#            if self.current_level_no < len(self.level_list)-1:
#                self.current_level_no += 1
#                self.current_level = self.level_list[self.current_level_no]
#                self.player.level = self.current_level
#        
#        
#    def display_frame(self, screen):
#        self.current_level.draw(screen)
#        self.active_sprite_list.draw(screen)    
#        
#        # Displaying coords
#        font = pygame.font.SysFont('Calibri', 35, True, False)
#        text = font.render(("x="+str(self.current_position)+"y="+str(self.player.rect.y)),
#                           True, constants.BLACK)
#        screen.blit(text, [30, 30])
#        
#        pygame.display.flip()






        
def main():
    """ Main Program """
    pygame.init()
 
    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Side-scrolling Platformer")
 
    # Create the player
    player = Player()
 
    # Create all the levels
    level_list = []
    level_list.append(levels.Level_01(player))
    level_list.append(levels.Level_02(player))
 
    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
 
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
 
    player.rect.x = 340
    player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
 
        # Update the player.
        active_sprite_list.update()
 
        # Update items in the level
        current_level.update()
 
        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)
 
        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)
 
        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        font = pygame.font.SysFont('Calibri', 15, True, False)
        text = font.render(("player.rect.x="+str(player.rect.x)+"\nplayer.rect.y="+str(player.rect.y)\
                            +"current_position="+str(current_position)+"current_level.world_shift"+\
                            str(current_level.world_shift)), True, constants.BLACK)
        screen.blit(text, [30, 30])
 
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
        # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
 
if __name__ == "__main__":
    main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#def main():
#    """ Main Program Function """
#    # Initialize pygame
#    pygame.init()
#    
#    # Set the window settings
#    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
#    screen = pygame.display.set_mode(size)
#    pygame.display.set_caption("CUNTRA")
#    
#    # Loop until the user clicks close button
#    done = False
#    
#    # Used to limit FPS
#    clock = pygame.time.Clock()
#    
#    # Create an instance of Game class
#    game = Game()
#    
#    # ---------- MAIN PROGRAM LOOP ---------- #
#    while not done:
#        # Process events
#        done = game.process_events()
#        
#        # Update object positions, check for collissions
#        game.run_logic()
#        
#        # Draw the current frame
#        game.display_frame(screen)
#        
#        # Limit FPS
#        clock.tick(60)
#        
#    pygame.quit()
#    
## Call the main function, start up the game
#if __name__ == "__main__":
#    main()