import pygame, random, csv, os
from config import *

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

#l = Levels('inn')
#print(l.maps_founder())
#print(l.layer_founder('inn').index('inn'+'_Ground'+'.csv'))