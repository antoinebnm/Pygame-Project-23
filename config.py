import pygame, random, sys, math, random, time, csv, os

PATH = os.path.dirname(__file__)
img_path = PATH + "/img/"
sprite_path = PATH + "/sprites/"
level_path = PATH + "/levels/"

###################################################################
#                                                                 #
#                        Window Settings                          #
#                                                                 #
###################################################################
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 380
LOWER_MARGIN = 0

#SCREEN_WIDTH = 1280
#SCREEN_HEIGHT = 640
#LOWER_MARGIN = 160

TILE_SIZE = 32
TILE_MARGIN = 0
SPRITE_SIZE = 64

FPS = 60

DEBUG = True


###################################################################
#                                                                 #
#                         Layers Levels                           #
#                                                                 #
###################################################################
PLAYER_LAYER = 1
GROUND_LAYER = 0


###################################################################
#                                                                 #
#                    Movements and Charcaters                     #
#                                                                 #
###################################################################
PLAYER_SPEED = 2
PLAYER_RUN = 5

PLAYER_CHARACTER = 'knight'


###################################################################
#                                                                 #
#                             KEYBINDS                            #
#                                                                 #
###################################################################
PLAYER_LEFT_KEY = pygame.K_LEFT
PLAYER_RIGHT_KEY = pygame.K_RIGHT
PLAYER_UP_KEY = pygame.K_UP
PLAYER_DOWN_KEY = pygame.K_DOWN


window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + LOWER_MARGIN))
screen = pygame.rect.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)