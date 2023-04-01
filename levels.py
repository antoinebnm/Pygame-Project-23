from config import *

class Levels:
    def __init__(self, map_level):
        self.map = map_level

    def maps_founder(self):
        self.maps = []
        for dir in os.listdir(level_path):
            self.maps.append(dir)
        return self.maps

    def layer_founder(self):
        self.layers = []
        for file in os.listdir(level_path + self.map + '/layers/'):
            self.layers.append(file)
        return self.layers
        
    def load_order(self):
        load_order = []
        map_layers = self.layer_founder(self.map)
        for map_layer in map_layers:
            for i in range(len(map_layers)):
                if i <10:
                    if map_layer.startwith('Layer_000' + i):
                        layer = map_layer
                elif i>9 and i<100:
                    if map_layer.startwith('Layer_00' + i):
                        layer = map_layer                  
                load_order.append(layer)
        return load_order