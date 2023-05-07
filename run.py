#!/usr/bin/python
# -*- coding: utf-8 -*-

from game import *

game = Game()
while game.running:
    game.run()

# Quit Pygame when the game loop exits
pygame.quit()