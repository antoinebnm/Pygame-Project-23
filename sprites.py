import pygame, random, math, sys

from levels import *
from tilesheet import *
from config import *

class Sprite():
    def __init__(self, view, scale):
        self._layer = PLAYER_LAYER
        self.sprite_animation = 'stand'
        self.num_tileset = 0
        self.view = view

        self.w = TILE_SIZE
        self.h = TILE_SIZE

        self.scale = scale

    #   Need to call Tilesheet here 'cause of the colliders check
        self.tiles = Map()

# Var de position x, y du joueur
        self.player_facing = "right"
        self.sprite_frame = 1
        self.facing_sprite = 10

        if self.view == 2:
            self.x = SCREEN_WIDTH // 400
            self.y = self.tiles.ground
        elif self.view == 2.5:
            self.x = SCREEN_WIDTH // 30
            self.y = SCREEN_HEIGHT // 2

        self.load_player_sprite()
        self.player_collider = pygame.rect.Rect(self.player_sprite.get_rect(topleft=(self.x + 16, self.y + 48), width=24, height=16))


# Chargement tileset du chararcter / à automatiser avec interface
    def load_player_sprite(self, sprite_name=PLAYER_CHARACTER):
        self.player_sprites = self.load_sprites((sprite_name + '_' + str(self.num_tileset) + '.png'))
        self.player_sprite = self.get_sprite(self.sprite_frame, self.facing_sprite)

# Suite du chargement et mise en variable
    def load_sprites(self, filename, rows = 21, cols = 13):
        image = pygame.image.load((sprite_path + filename)).convert() # Save des perfs, add .convert()
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
    def draw_sprite(self,x,y):
        self.player_sprite = self.get_sprite(self.sprite_frame, self.facing_sprite)
        self.player_sprite = pygame.transform.scale(self.player_sprite, (((int(self.player_sprite.get_width())*self.scale)),(int(self.player_sprite.get_height())*self.scale)))
        self.player_collider = self.player_sprite.get_rect(topleft=(x + 16, y + 48), width=24, height=16)

# FONCTION UPDATE / récurrence
    def update(self, COUNTER):
        self.movements()
        self.animation(COUNTER)

# redraw du sprite après check de l'animation
        self.draw_sprite(self.x,self.y)

    def animation(self, COUNTER):
        if self.sprite_animation == 'walk':
            if self.player_facing == 'left':
                self.facing_sprite = 10
            elif self.player_facing == 'right':
                self.facing_sprite = 12

        keys = pygame.key.get_pressed()

        if (keys[PLAYER_LEFT_KEY] or keys[PLAYER_RIGHT_KEY]):
            self.sprite_animation = 'walk'
        else:
            self.sprite_animation = 'stand'

        self.animate_frames(COUNTER)

    def animate_frames(self, COUNTER):
        if self.sprite_animation == 'walk':
            if (self.sprite_frame < 9):
                if ((COUNTER % 6)==0):
                    self.sprite_frame += 1
            else:
                self.sprite_frame = 1
        if self.sprite_animation == 'stand':
            self.sprite_frame = 1

    def movements(self):
        keys = pygame.key.get_pressed()
        if keys[PLAYER_RIGHT_KEY]:
            self.tiles.scroll_map(1)