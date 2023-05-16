import pygame, random, sys, math, random, time, csv, os, json, threading

#from pygame.locals import *

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
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_desktop_sizes()[0][0]*0.8,pygame.display.get_desktop_sizes()[0][1]*0.8
LOWER_MARGIN = SCREEN_HEIGHT // 2.6
SCREEN_HEIGHT -= LOWER_MARGIN


TILE_SIZE = 32
TILE_MARGIN = 0
SPRITE_SIZE = 64

FPS = 60

RESIZE = False
DEBUG = False
SAVE = False

if RESIZE:
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + LOWER_MARGIN),pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
else:
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + LOWER_MARGIN),pygame.HWSURFACE | pygame.DOUBLEBUF)
screen = pygame.rect.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)


icon = pygame.image.load(img_path + 'elve_char.png')
pygame.display.set_icon(icon)

# font
pygame.font.init()
font = pygame.font.Font((fonts_path + '8bit_wonder/8-BITWONDER.ttf'),16)

clock = pygame.time.Clock()


###################################################################
#                                                                 #
#                     Thread Parallel Tasks                       #
#                                                                 #
###################################################################
from concurrent.futures import ThreadPoolExecutor

def run_io_tasks_in_parallel(tasks):
    with ThreadPoolExecutor() as executor:
        running_tasks = [executor.submit(task) for task in tasks]
        for running_task in running_tasks:
            try:
                running_task.result()
            except TypeError:
                pass
        
        executor.shutdown()
"""
print(ThreadPoolExecutor()._max_workers)

run_io_tasks_in_parallel([
    lambda: funcA(),
    lambda: funcB(),
])
"""

###################################################################
#                                                                 #
#                             Colors                              #
#                                                                 #
###################################################################
COLOR_UI = pygame.color.Color(20, 23, 37)
COLOR_WHITE = pygame.color.Color(255,255,255)
COLOR_MENU = pygame.color.Color(20,160,130)


###################################################################
#                                                                 #
#                         Layers Levels                           #
#                                                                 #
###################################################################
MAP_VIEW = 2

GROUND_LEVEL = SCREEN_HEIGHT - ((LOWER_MARGIN)//(3.3)) - 8


###################################################################
#                                                                 #
#                    MOVEMENTS and Charcaters                     #
#                                                                 #
###################################################################
PLAYER_SPEED = SCREEN_WIDTH / 500
PLAYER_RUN = SCREEN_WIDTH / 320
UI_SCALE = (SCREEN_WIDTH*SCREEN_HEIGHT) // 810000

PLAYER_CHARACTERS = ['warrior','elve','healer','mage'] # warrior, elve, mage, healer

HEROES_ACTIONS_BUFFS = {
    'Basic': None,
    'Basic Slash' : False,
    'Knife Cut' : False,
    'Wand Swing' : False,
    'Fire Ball' : False,

    'Secondary': None,
    'Jump Slash' : {'Damage': +0.2, 'Armor': -0.1},
    'Arrow Shot' : {'Ammo': -1},
    'Heal' : {'Heal': +0.2},
    'Weakening Spell' : {'Enemy Strength': -0.2},
    
    'Special': None,
    'Spinning Attack' : {'Cooldown': +1},
    'Piercing Arrow' : {'Damage': +0.2, 'Ammo': -1, 'Cooldown': +1},
    'Revive' : {'Cooldown': +2, 'Heal': +0.4},
    'Growing Roots' : {'Enemy Armor': -0.2},

    'Defense' : {'Armor': +0.3}
}

INVENTORY = {
    'Money': 0,
    'Heal Potions': 0,
    'Warrior Upgrade': False,
    'Archer Upgrade': False,
    'Healer Upgrade': False,
    'Mage Upgrade': False
}

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