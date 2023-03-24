from tilesheet import *
from levels import *
from sprites import *
from config import *

class Game:
    def __init__(self):
        # Initialize Pygame and game objects
        pygame.init()
        
        window.fill(pygame.Color(180, 120, 60))
        self.clock = pygame.time.Clock()
        self.menu = False
        self.running = True
        self.COUNTER = 0

### Fonction initialisation d'une nouvelle partie
    def new_game(self):
        window.fill(pygame.Color(0,0,0), screen)
        self.playing = True

    #   Call Player class in Sprites
        self.player = Sprite(1,1)


### Fonction récurente pour actualiser l'écran
    def draw_window(self):
        self.player.tiles.draw_map()

        # Load ALL Sprite at the very end ==> else : will not appear on screen
        window.blit(self.player.player_sprite, (self.player.x, self.player.y))
        if DEBUG:
            window.fill(pygame.color.Color(255,0,0), self.player.player_collider)
        # ___________________________________

    # Handle user input events
    def events(self):
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                pygame.quit()
        
        if not self.menu:
            if self.keys[pygame.K_ESCAPE]:
                image = pygame.image.load((img_path + 'mc_pausescreen' + '.png')).convert()
                image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
                self.menu = True
                window.fill(pygame.color.Color(0,0,0))
                window.blit(image, screen)
        if self.menu:
            if self.keys[pygame.K_SPACE]:
                self.menu = False

    # Update the game state based on user input and object behavior
    def update(self):
        self.player.update(self.COUNTER)
        if DEBUG:
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