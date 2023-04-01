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
# 1600x900 | 1440×900 | 1280×720 
SCREEN_WIDTH, SCREEN_HEIGHT = 900,900
LOWER_MARGIN = 0

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
PLAYER_SPEED = SCREEN_WIDTH / 500
PLAYER_RUN = SCREEN_WIDTH / 320
UI_SCALE = (SCREEN_WIDTH*SCREEN_HEIGHT) // 120000

PLAYER_CHARACTER = 'warrior'


###################################################################
#                                                                 #
#                             KEYBINDS                            #
#                                                                 #
###################################################################
PLAYER_LEFT_KEY = pygame.K_LEFT
PLAYER_RIGHT_KEY = pygame.K_RIGHT
PLAYER_UP_KEY = pygame.K_UP
PLAYER_DOWN_KEY = pygame.K_DOWN


window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + LOWER_MARGIN), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
screen = pygame.rect.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)