import pygame, random, csv, os
from config import *

# Chargement du chemin d'accès absolu en variable globale
path = os.path.dirname(__file__) + "/levels/"

class Levels:
    def __init__(self, map_level, screen=(pygame.rect.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))):
        self.screen = screen
        self.map = map_level

    def maps_founder(self):
        self.maps = []
        for dir in os.listdir(path):
            self.maps.append(dir)
        return self.maps

    def layer_founder(self, LevelNameStart, LevelNameEnd=('.csv')):
        self.LevelNameStart = LevelNameStart
        self.LevelNameEnd = LevelNameEnd

        self.layers = []
        for file in os.listdir(path + self.map):
            if ((file.startswith(LevelNameStart)) and (file.endswith(LevelNameEnd))):
                self.layers.append(file)
        return self.layers
    
    def load_order(self):
        load_order = []
        map_layers = self.layer_founder(self.map)
        for map_layer in map_layers:
            if map_layer == (self.map + '_Ground.csv'):
                load_order.insert(0, map_layer)
            if map_layer == (self.map + '_Walls.csv'):
                load_order.insert(1, map_layer)
            if map_layer == (self.map + '_Objects.csv'):
                load_order.insert(1, map_layer)
            if map_layer == (self.map + '_Trees.csv'):
                load_order.insert(1, map_layer)
        return load_order