import pygame, random, math, sys
from config import *

path = os.path.dirname(__file__) + "/sprites/"

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y= y * TILE_SIZE
        self.w = TILE_SIZE
        self.h = TILE_SIZE

        self.x_move = 0
        self.y_move = 0
        self.player_facing = "down"

        self.image = pygame.Surface([self.w, self.h])
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def load_player_sprite(self):
        self.image = pygame.image.load(path + 'player.png')
        surface = pygame.Surface(self.image.get_size())
        surface.blit(self.image, self.player_pos)
        
        player_sprites = PlayerSprite('knight.png', 832, 1344, 21, 13)
        self.player_sprite = player_sprites.get_sprite(1, 10)

    def update(self):
        self.movements()
        
        self.rect.x += self.x_move
        self.rect.y += self.y_move

        self.x_move = 0
        self.y_move = 0

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

class PlayerSprite():
    def __init__(self, filename, width, height, rows, cols):
        image = pygame.image.load((path + filename)).convert()
        self.sprite_table = []
        for tile_x in range(0, cols):
            line = []
            self.sprite_table.append(line)
            for tile_y in range(0, rows):
                rect = (tile_x * SPRITE_SIZE, tile_y * SPRITE_SIZE, SPRITE_SIZE, SPRITE_SIZE)
                line.append(image.subsurface(rect))
    
    def get_sprite(self, x, y):
        return self.sprite_table[x][y]

    def draw_sprite(self, screen, x ,y):
        self.sprite = self.get_sprite(0, 10)
        screen.blit(self.sprite, (x * SPRITE_SIZE, y * SPRITE_SIZE))
