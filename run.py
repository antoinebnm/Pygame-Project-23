#!/usr/bin/python
# -*- coding: utf-8 -*-

from game import *

game = Game()

###################################################################
#                                                                 #
#            Main Running loop (calls Main Game loop)             #
#                                                                 #
###################################################################
if __name__ == "__main__":
    while game.running:
        game.run()

    # Quit Pygame when the game loop exits
    pygame.quit()
