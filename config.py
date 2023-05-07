import pygame, random, sys, math, random, time, csv, os, json

PATH = os.path.dirname(__file__)
img_path = PATH + "/img/"
sprite_path = PATH + "/sprites/"
level_path = PATH + "/levels/"
fonts_path = PATH + "/fonts/"

pygame.display.init()

###################################################################
#                                                                 #
#                        Window Settings                          #
#                                                                 #
###################################################################
# 1600x900 | 1440×900 | 1280×720 
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_desktop_sizes()[0][0]-320,pygame.display.get_desktop_sizes()[0][1]-280
LOWER_MARGIN = SCREEN_HEIGHT // 4

TILE_SIZE = 32
TILE_MARGIN = 0
SPRITE_SIZE = 64

FPS = 60

icon = pygame.image.load(img_path + 'elve_char.png')
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + LOWER_MARGIN),pygame.HWSURFACE | pygame.DOUBLEBUF)# | pygame.RESIZABLE)
screen = pygame.rect.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
pygame.display.set_icon(icon)

# font
pygame.font.init()
font = pygame.font.Font((fonts_path + '8bit_wonder/8-BITWONDER.ttf'),16)

clock = pygame.time.Clock()


DEBUG = False


###################################################################
#                                                                 #
#                             Colors                              #
#                                                                 #
###################################################################
COLOR_UI = pygame.color.Color(20, 23, 37)
COLOR_WHITE = pygame.color.Color(255,255,255)


###################################################################
#                                                                 #
#                         Layers Levels                           #
#                                                                 #
###################################################################
MAP_VIEW = 2
ground_h = pygame.image.load(level_path + 'Forest/layers/ground_layer.png').convert_alpha().get_height()
GROUND_LEVEL = SCREEN_HEIGHT - ((LOWER_MARGIN + ground_h)//2) + 10


###################################################################
#                                                                 #
#                    MOVEMENTS and Charcaters                     #
#                                                                 #
###################################################################
PLAYER_SPEED = SCREEN_WIDTH / 500
PLAYER_RUN = SCREEN_WIDTH / 320
UI_SCALE = (SCREEN_WIDTH*SCREEN_HEIGHT) // 810000

PLAYER_CHARACTERS = ['warrior','elve','healer','mage'] # warrior, elve, mage, healer


###################################################################
#                                                                 #
#                             KEYBINDS                            #
#                                                                 #
###################################################################
PLAYER_LEFT_KEY = pygame.K_LEFT
PLAYER_RIGHT_KEY = pygame.K_RIGHT
PLAYER_UP_KEY = pygame.K_UP
PLAYER_DOWN_KEY = pygame.K_DOWN



if DEBUG:
    print('ground lvl',GROUND_LEVEL, 'lower marg.',LOWER_MARGIN)
    print('width',SCREEN_WIDTH,'height',SCREEN_HEIGHT)