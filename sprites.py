import pygame, random, math, sys
from config import *

# Chargement du chemin d'accès absolu en variable globale
path = os.path.dirname(__file__) + "/sprites/"
screen = pygame.rect.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
game_screen = pygame.surface.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

class Player():
    def __init__(self, x, y):
        self._layer = PLAYER_LAYER

        self.x = x * TILE_SIZE
        self.y= y * TILE_SIZE
        self.w = TILE_SIZE
        self.h = TILE_SIZE

# Var de position x, y du joueur
        self.player_pos = (self.x, self.y)

        self.x_move = 0
        self.y_move = 0
        self.player_facing = "down"
        self.facing_sprite = 10

# à changer / automatiser avec interface
        self.load_player_sprite()

# Chargement tileset du chararcter / à automatiser avec interface
    def load_player_sprite(self, sprite_name=PLAYER_CHARACTER):
        self.player_sprites = self.load_sprites((sprite_name + '.png'), 832, 1344)

# Suite du chargement et mise en variable
    def load_sprites(self, filename, width, height, rows = 21, cols = 13):
        image = pygame.image.load((path + filename)).convert() # Save des perfs, add .convert()
        self.sprite_table = []
        for tile_x in range(0, cols):
            line = []
            self.sprite_table.append(line)
            for tile_y in range(0, rows):
                rect = (tile_x * SPRITE_SIZE, tile_y * SPRITE_SIZE, SPRITE_SIZE, SPRITE_SIZE) # tiles x&y * 2 ==> TILE_SIZE * 2 = SPRITE_SIZE
                line.append(image.subsurface(rect))
    
# Fonction de récup. de tile, tout est dans le nom
    def get_sprite(self, x_char=1, y_char=10):
        return self.sprite_table[x_char - 1][y_char - 1]

# Dessiner le character sur l'écran (.blit)
    def draw_sprite(self):
        self.player_sprite = self.get_sprite(1, self.facing_sprite)


# FONCTION UPDATE / récurrence
    def update(self):
        self.movements()
        self.animation()
        
# pos_move calculé par .movements()
        self.x += self.x_move
        self.y += self.y_move

# redraw du sprite après check de l'animation
        self.draw_sprite()

        self.x_move = 0
        self.y_move = 0


    def animation(self):
        if self.player_facing == 'up':
            self.facing_sprite = 9
        elif self.player_facing == 'left':
            self.facing_sprite = 10
        elif self.player_facing == 'down':
            self.facing_sprite = 11
        elif self.player_facing == 'right':
            self.facing_sprite = 12


    def movements(self):
        keys = pygame.key.get_pressed()

        if keys[PLAYER_LEFT_KEY]:
            self.x_move -= PLAYER_SPEED
            self.player_facing = "left"
        if keys[PLAYER_RIGHT_KEY]:
            self.x_move += PLAYER_SPEED
            self.player_facing = "right"
        if keys[PLAYER_UP_KEY]:
            self.y_move -= PLAYER_SPEED
            self.player_facing = "up"
        if keys[PLAYER_DOWN_KEY]:
            self.y_move += PLAYER_SPEED
            self.player_facing = "down"