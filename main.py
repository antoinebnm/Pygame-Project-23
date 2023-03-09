import pygame, random, sys
from tilesheet import *
from sprites import *
from config import *

path = os.path.dirname(__file__)

class Game:
    def __init__(self):
        # Initialize Pygame and game objects
        pygame.init()
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + LOWER_MARGIN))
        self.screen = pygame.rect.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.window.fill(pygame.Color(195, 142, 50, 60))
        self.clock = pygame.time.Clock()
        self.running = True

        self.tiles = Tilesheet('tilemap.png', 1024, 2016, 63, 32)

    # Define game functions
    def random_tiles(self):
        for i in range(self.screen.left, self.screen.right, TILE_SIZE):
            for j in range(self.screen.top, self.screen.bottom, TILE_SIZE):
                self.window.blit(self.tiles.get_tile(random.randint(0,31), random.randint(0,62)), (i, j))

    def new_game(self):
        self.playing = True
        self.player = Player(0,10)

    def draw_window(self):
        self.window.fill(pygame.Color(0,0,0), self.screen)

        for i in range(self.screen.left, self.screen.right, TILE_SIZE):
            for j in range(self.screen.top, self.screen.bottom, TILE_SIZE):
                self.window.blit(self.tiles.get_tile(8, 2), (i, j))

        if self.keys[pygame.K_r]:
            self.random_tiles()

        # Load ALL Sprite at the very end ==> else : will not appear on screen
        self.player.update()
        self.player.draw_sprite()
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
        
        #pygame.display.set_caption("{:.2f} FPS".format(self.clock.get_fps()))
        pass

    # Main game loop
    def main(self):

        while self.playing:
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