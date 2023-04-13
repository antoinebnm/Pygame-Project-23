import pygame, random, sys, math, random, time, csv, os

PATH = os.path.dirname(__file__)
img_path = PATH + "/img/"
sprite_path = PATH + "/sprites/"
level_path = PATH + "/levels/"

pygame.display.init()

###################################################################
#                                                                 #
#                        Window Settings                          #
#                                                                 #
###################################################################
# 1600x900 | 1440×900 | 1280×720 
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_desktop_sizes()[0][0]-320,pygame.display.get_desktop_sizes()[0][1]-280
LOWER_MARGIN = 180

TILE_SIZE = 32
TILE_MARGIN = 0
SPRITE_SIZE = 64

FPS = 60

DEBUG = False

COLOR_UI = pygame.color.Color(20, 23, 37)


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
UI_SCALE = (SCREEN_WIDTH*SCREEN_HEIGHT) // 810000

PLAYER_CHARACTERS = ['warrior','elve','mage'] # warrior, elve, mage, healer


###################################################################
#                                                                 #
#                             KEYBINDS                            #
#                                                                 #
###################################################################
PLAYER_LEFT_KEY = pygame.K_LEFT
PLAYER_RIGHT_KEY = pygame.K_RIGHT
PLAYER_UP_KEY = pygame.K_UP
PLAYER_DOWN_KEY = pygame.K_DOWN

icon = pygame.image.load(img_path + 'elve_char.png')
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + LOWER_MARGIN), pygame.HWSURFACE | pygame.DOUBLEBUF)# | pygame.RESIZABLE)
screen = pygame.rect.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
pygame.display.set_icon(icon)

clock = pygame.time.Clock()