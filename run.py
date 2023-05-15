#!/usr/bin/python
# -*- coding: utf-8 -*-

from game import *

#FightSyst.main(0)

game = Game()

while game.running:
    game.run()

# Quit Pygame when the game loop exits
pygame.quit()