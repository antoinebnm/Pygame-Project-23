from config import *
from levels import *

class Tilesheet:
# Chargement tileset du chararcter / à automatiser avec interface
    def __init__(self, filename, rows, cols):
        image = pygame.image.load((img_path + filename)).convert()
        self.tile_table = []
        for tile_x in range(0, cols):
            line = []
            self.tile_table.append(line)
            for tile_y in range(0, rows):
                rect = pygame.rect.Rect(tile_x * TILE_SIZE, tile_y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                line.append(image.subsurface(rect))
        
        self.tile_collider = pygame.rect.Rect((0, 0), (TILE_SIZE, TILE_SIZE))

        self.level = Levels('inn')
        self.load_order = self.level.load_order()

# Fonction de récup. de tile, tout est dans le nom
    def get_tile(self, x, y):
        return self.tile_table[x][y]

# Dessiner le character sur l'écran (.blit)
    def draw_tiles(self, screen):
        for x, row in enumerate(self.tile_table):
            for y, tile in enumerate(row):
                screen.blit(tile, (x * TILE_SIZE, y * TILE_SIZE))

    def draw_map(self):
# Draw tilemap on screen
        tile_colliders = []
        for i in self.load_order:
            with open(level_path + self.level.map + '/' + i) as level_csv:
                level_csv = csv.reader(level_csv)
                for x, rows in enumerate(level_csv):
                    for y, id in enumerate(rows):
                        if id == '-1':
                            pass
                        else :
                            window.blit(self.get_tile(int(id) % TILE_SIZE, int(id) // TILE_SIZE), (y * TILE_SIZE, x * TILE_SIZE))
                        #print('x : ', x, ' y : ', y, ' row : ', rows, ' id : ', id)
                        if i == 'inn_Walls.csv':
                            if id == '276' or id == '277' or id == '308' or id == '309':
                                self.tile_collider.topleft = y * TILE_SIZE, x * TILE_SIZE
                                tile_colliders.append(pygame.rect.Rect(self.tile_collider.left,self.tile_collider.top,32,32))
                                if DEBUG:
                                    window.fill(pygame.color.Color(0,0,255), self.tile_collider)
        self.map_colliders = tile_colliders