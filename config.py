###################################################################
#                                                                 #
#                         Imports and Paths                       #
#                                                                 #
###################################################################
import pygame, random, sys, math, random, time, csv, os, json, threading

PATH = os.path.dirname(__file__)
img_path = PATH + "/img/"
sprite_path = PATH + "/sprites/"
level_path = PATH + "/levels/"
fonts_path = PATH + "/fonts/"

pygame.display.init()

###################################################################
#                                                                 #
#                        Window Variables                         #
#                                                                 #
###################################################################
# 1600x900 | 1440×900 | 1280×720 
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_desktop_sizes()[0][0]*0.8,pygame.display.get_desktop_sizes()[0][1]*0.8
LOWER_MARGIN = SCREEN_HEIGHT // 2.6
CONSOLE_WIDTH = int(SCREEN_WIDTH * 0.6)
SCREEN_HEIGHT -= LOWER_MARGIN


TILE_SIZE = 32
TILE_MARGIN = 0
SPRITE_SIZE = 64

FPS = 60

RESIZE = False
DEBUG = False
SAVE = False


###################################################################
#                                                                 #
#                          Window Settings                        #
#                                                                 #
###################################################################
if RESIZE:
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + LOWER_MARGIN),pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
else:
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + LOWER_MARGIN),pygame.HWSURFACE | pygame.DOUBLEBUF)

console = pygame.rect.Rect(SCREEN_WIDTH - CONSOLE_WIDTH, 0, CONSOLE_WIDTH, SCREEN_HEIGHT)
screen = pygame.rect.Rect(0, 0, SCREEN_WIDTH - CONSOLE_WIDTH, SCREEN_HEIGHT)


icon = pygame.image.load(img_path + 'icon.png')
pygame.display.set_icon(icon)

# font
pygame.font.init()
font = pygame.font.Font((fonts_path + '8bit_wonder/8-BITWONDER.ttf'),16)

clock = pygame.time.Clock()


###################################################################
#                                                                 #
#                   Thread simultaneously Tasks                   #
#                                                                 #
###################################################################
from concurrent.futures import ThreadPoolExecutor

def run_io_tasks_in_simultaneously(tasks):
    with ThreadPoolExecutor() as executor:
        running_tasks = [executor.submit(task) for task in tasks]
        for running_task in running_tasks:
            try:
                running_task.result()
            except TypeError:
                pass
        
        executor.shutdown()
"""     ⬇︎ HOW TO CALL FUCTION ⬇︎

run_io_tasks_in_simultaneously([
    lambda: funcA(),
    lambda: funcB(),
])
"""

###################################################################
#                                                                 #
#                             Colors                              #
#                                                                 #
###################################################################
class Color():
    blank = '\u001b[0m'
    black = '\u001b[30m'
    red = '\u001b[31m'
    green = '\u001b[32m'
    yellow = '\u001b[33m'
    blue = '\u001b[34m'
    magenta = '\u001b[35m'
    cyan = '\u001b[36m'

# PYGAME COLORS
COLOR_UI = pygame.color.Color(19, 22, 35)
COLOR_WHITE = pygame.color.Color(255,255,255)
COLOR_BLACK = pygame.color.Color(0,0,0)
COLOR_MENU = pygame.color.Color(20,160,130)


###################################################################
#                                                                 #
#                         Other Variables                         #
#                                                                 #
###################################################################
MAP_VIEW = 2

GROUND_LEVEL = SCREEN_HEIGHT - ((LOWER_MARGIN)//(3.3)) - 8

PLAYER_SPEED = SCREEN_WIDTH / 500
PLAYER_RUN = SCREEN_WIDTH / 320
UI_SCALE = (SCREEN_WIDTH*SCREEN_HEIGHT) // 810000



###################################################################
#                                                                 #
#                 Heroes, statistics and inventory                #
#                                                                 #
###################################################################
# Guerrier, Chasseur, Guerisseur, Mage
# Stats : [Health, Attack turn, Damage, Armor, Ammo]
PLAYER_CHARACTERS = {
    'Guerrier': [20,1,14,0.4, None],
    'Chasseur': [18,3,12,0.8,5],
    'Guerisseur': [16,5,8,1.1, None],
    'Mage': [16,4,14,0.9, None]
}

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