# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 10:47:06 2017

@author: anonymous
"""

import pygame
import random

# ----- GLOBAL CONSTANTS ----- #
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

# ----- CLASSES ----- #
class Block(pygame.sprite.Sprite):
    """ This class represents a simple block the player collects """
    def __init__(self):
        """ Constructor, create the image of the block """
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        
    def reset_pos(self):
        """ Called when the block is 'collected' or falls off the screen """
        self.rect.x = random.randrange(SCREEN_WIDTH)
        self.rect.y = random.randrange(-300, -20)
        
    def update(self):
        """ Automaticallyy called when we need to move the block """
        self.rect.y += 1
        
        if self.rect.y > SCREEN_HEIGHT + self.rect.height:
            self.reset_pos()
            
class Player(pygame.sprite.Sprite):
    """ This class represents the player """
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        
    def update(self):
        """ Update the player locaion """
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        
class Game(object):
    """ This class represents an instance of the game. If we need to reset
    the game we'd just need to create a new instance of this class """
    def __init__(self):
        """ Constructor. Create all atributes and initialize the game """
        self.score = 0
        self.game_over = False
        
        # Create sprite list
        self.block_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
        
        # Create the block sprites
        for i in range(50):
            block = Block()
            
            block.rect.x = random.randrange(SCREEN_WIDTH)
            block.rect.y = random.randrange(-300, SCREEN_HEIGHT)
            
            self.block_list.add(block)
            self.all_sprites_list.add(block)
            
        # Create the player
        self.player = Player()
        self.all_sprites_list.add(self.player)
        
    def process_events(self):
        """ Process all of the events. Return a "True" if we need
        to close the window """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()
                    
        return False
        
    def run_logic(self):
        """ This method is run each time through the frame.
        It updates positions and checks for collisions. """
        if not self.game_over:
            # Move all the sprites
            self.all_sprites_list.update()
            
            # See if the player block has collided with anything
            block_hit_list = pygame.sprite.spritecollide(self.player, self.block_list, True)
            
            # Check the list of collisions
            for block in block_hit_list:
                self.score += 1
                print(self.score)
                if self.score == 50:
                    self.game_over = True
                # (TIP!) You can do something with block here
        
    def display_frame(self, screen):
        """ Display everything to the screen for the game """
        screen.fill(WHITE)
        
        if self.game_over:
            # font = pygame.font.Font("Serif", 25)
            font = pygame.font.SysFont("serif", 25)
            text = font.render("Game over. Click to restart.", True, BLACK)
            center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
            center_y = (SCREEN_HEIGHT // 2) - (text.get_width() // 2)
            screen.blit(text, [center_x, center_y])
            
        else:
            self.all_sprites_list.draw(screen)
        
        pygame.display.flip()
        
def main():
    """ Main program function """
    # Initialize pygame and setup the window
    pygame.init()
    
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    
    pygame.display.set_caption("My Game")
    pygame.mouse.set_visible(False)
    
    # Create our objects and set the ata
    done = False
    clock = pygame.time.Clock()
    
    # Create an instance of the Game class
    game = Game()
    
    # Main game loop
    while not done:
        # Process events (keystrokes, mouse clicks, etc)
        done = game.process_events()
        
        # Update object positions, check for collisions
        game.run_logic()
        
        # Draw the current frame
        game.display_frame(screen)
        
        # Pause for the next frame
        clock.tick(60)
        
    # Close the window and exit
    pygame.quit()
    
# Call the main function, start up the game
if __name__ == "__main__":
    main()