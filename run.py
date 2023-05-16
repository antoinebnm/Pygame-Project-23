#!/usr/bin/python
# -*- coding: utf-8 -*-

from game import *

game = Game()


class Color():
    blank = '\033[0m'
    red = '\033[31m'
    green = '\033[92m'


print(Color.green + """
                        .@ 
                      .@@@
                    .@@@@'
                   .@@@@'
                   @@@'
                   @'""" + Color.red +"""
      .@@@@@@@@@@@. .@@@@@@@@@@@.
   .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.
 .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.
.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.
`@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.
 `@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
  `@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
   `@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
     `@@@@@@@@@@@@@@@@@@@@@@@@@@@'
       `@@@@@@@@@@@@@@@@@@@@@@@'
         `@@@@@@@@@''@@@@@@@@'
""" + Color.blank)

if __name__ == "__main__":
    while game.running:
        game.run()

    # Quit Pygame when the game loop exits
    pygame.quit()
