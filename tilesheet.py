import sys, os, pygame
from config import *

path = os.path.dirname(__file__)
levels_path = path + "/levels/"

class Tilesheet:
    def __init__(self, filename, width, height, rows, cols):
        image = pygame.image.load((path + '/img/' + filename)).convert()
        self.tile_table = []
        for tile_x in range(0, cols):
            line = []
            self.tile_table.append(line)
            for tile_y in range(0, rows):
                rect = (tile_x * TILE_SIZE, tile_y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                line.append(image.subsurface(rect))
    
    def get_tile(self, x, y):
        return self.tile_table[x][y]

    def draw_tiles(self, screen):
        for x, row in enumerate(self.tile_table):
            for y, tile in enumerate(row):
                screen.blit(tile, (x * TILE_SIZE, y * TILE_SIZE))
