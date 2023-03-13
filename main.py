import pygame, random, sys
from tilesheet import *
from levels import *
from sprites import *
from config import *

# Chargement du chemin d'accès absolu en variable globale
path = os.path.dirname(__file__)

class Game:
    def __init__(self):
        # Initialize Pygame and game objects
        pygame.init()
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + LOWER_MARGIN))
        self.screen = pygame.rect.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.window.fill(pygame.Color(180, 120, 60))
        self.clock = pygame.time.Clock()
        self.running = True
        self.COUNTER = 0

        self.tiles = Tilesheet('tilemap.png', 1024, 2016, 63, 32)

    # Define game functions
    def random_tiles(self):
        for i in range(self.screen.left, self.screen.right, TILE_SIZE):
            for j in range(self.screen.top, self.screen.bottom, TILE_SIZE):
                self.window.blit(self.tiles.get_tile(random.randint(0,31), random.randint(0,62)), (i, j))

### Fonction initialisation d'une nouvelle partie
    def new_game(self):
        self.playing = True
        self.player = Player(1,1)

        self.level = Levels('inn')
        self.load_order = self.level.load_order()


### Fonction récurente pour actualiser l'écran
    def draw_window(self):
        self.window.fill(pygame.Color(0,0,0), self.screen)
        self.draw_map()

    def draw_map(self):
# Draw tilemap on screen

        #for i in range(self.screen.left, self.screen.right, TILE_SIZE):
        #    for j in range(self.screen.top, self.screen.bottom, TILE_SIZE):
        #        self.window.blit(self.tiles.get_tile(8, 2), (i, j))
        
        for i in self.load_order:
            with open(path + '/levels/' + self.level.map + '/' + i) as level_csv:
                level_csv = csv.reader(level_csv)
                for x, rows in enumerate(level_csv):
                    for y, id in enumerate(rows):
                        if id == '-1':
                            pass
                        else :
                            self.window.blit(self.tiles.get_tile(int(id) % TILE_SIZE, int(id) // TILE_SIZE), (y * TILE_SIZE, x * TILE_SIZE))
                        #print('x : ', x, ' y : ', y, ' row : ', rows, ' id : ', id)

# Random function ==> pour le fun (epilepsie)
        if self.keys[pygame.K_r]:
            self.random_tiles()

        # Load ALL Sprite at the very end ==> else : will not appear on screen
        self.player.update(self.COUNTER)
        self.window.blit(self.player.player_sprite, (self.player.x, self.player.y))
        # ___________________________________

        pygame.display.flip()

    # Handle user input events
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                pygame.quit()
        
        self.keys = pygame.key.get_pressed()

    # Update the game state based on user input and object behavior
    def update(self):
        pygame.display.set_caption("Facing %s" % (self.player.player_facing))
        #pygame.display.set_caption("{:.2f} FPS".format(self.clock.get_fps()))
        pass

    # Main game loop
    def main(self):

        while self.playing:
            self.COUNTER += 1

            self.events()
            self.update()

            self.draw_window()

            # Update display and tick clock
            pygame.display.update()
            self.clock.tick(FPS)
        
        self.running = False

g = Game()
g.new_game()
while g.running:
    g.main()

# Quit Pygame when the game loop exits
pygame.quit()