#!/usr/bin/python
# -*- coding: utf-8 -*-

from game import *

game = Game()

if __name__ == "__main__":
    while game.running:
        game.run()


#game.run()
        
    # Quit Pygame when the game loop exits
    pygame.quit()