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
        self.menu = False
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
        self.window.fill(pygame.Color(0,0,0), self.screen)
        self.playing = True
        self.player = Sprite(1,1)

        self.level = Levels('inn')
        self.load_order = self.level.load_order()


### Fonction récurente pour actualiser l'écran
    def draw_window(self):
        self.draw_map()

        # Load ALL Sprite at the very end ==> else : will not appear on screen
        self.window.blit(self.player.player_sprite, (self.player.x, self.player.y))
        self.window.fill(pygame.color.Color(255,0,0), self.player.player_collider)
        # ___________________________________

    def draw_map(self):
# Draw tilemap on screen
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
                        if i == 'inn_Walls.csv':
                            if id == '276' or id == '277' or id == '308' or id == '309':
                                self.tiles.tile_collider.topleft = y * TILE_SIZE, x * TILE_SIZE
                                self.window.fill(pygame.color.Color(0,0,255), self.tiles.tile_collider)

# Random function ==> pour le fun (epilepsie)
        if self.keys[pygame.K_r]:
            self.random_tiles()

    # Handle user input events
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                pygame.quit()
        
        if not self.menu:
            if self.keys[pygame.K_ESCAPE]:
                self.menu = True
                self.window.fill(pygame.color.Color(255,255,255))
        if self.menu:
            if self.keys[pygame.K_SPACE]:
                self.menu = False
    
    def ifcollision(self):
        dx = 0
        dy = 0
        player_collider = self.player.player_collider
        tile_collider = self.tiles.tile_collider
        if player_collider.colliderect(tile_collider):
            if player_collider.top >= tile_collider.bottom:
                dy = tile_collider.bottom - player_collider.top
            if player_collider.left <= tile_collider.right:
                dx = tile_collider.right - player_collider.left
            if player_collider.right >= tile_collider.left:
                dx = tile_collider.left - player_collider.right
            if player_collider.bottom <= tile_collider.top:
                dy = tile_collider.top - player_collider.bottom
            print(dx, dy)
    # Correct Player position ==> can move freely again
        self.player.correct_xy(dx, dy)


    # Update the game state based on user input and object behavior
    def update(self):
        self.ifcollision()
        self.player.update(self.COUNTER)
        pygame.display.set_caption("Facing %s" % (self.player.player_facing))
        #pygame.display.set_caption("{:.2f} FPS".format(self.clock.get_fps()))

    # Main game loop
    def main(self):

        while self.playing:
            self.keys = pygame.key.get_pressed()
            self.COUNTER += 1
            
            self.events()
            
            if not self.menu:
                self.draw_window()
                self.update()
            

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