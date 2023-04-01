from tilesheet import *
from levels import *
from sprites import *
from config import *
from button import *

clock = pygame.time.Clock()


#button images
start_img = pygame.image.load(img_path + 'start_btn.png').convert()
exit_img = pygame.image.load(img_path + 'exit_btn.png').convert()
start_button = Button(SCREEN_WIDTH // 2 - 130, SCREEN_HEIGHT // 2 - 150, start_img, 1)
exit_button = Button(SCREEN_WIDTH // 2 - 110, SCREEN_HEIGHT // 2 + 50, exit_img, 1)

class Game:
    def __init__(self):
        # Initialize Pygame and game objects
        pygame.init()
        
        window.fill(pygame.Color(0,0,0))
        self.menu = False
        self.playing = False
        self.running = True
        self.COUNTER = 0
        self.init_game = False

### Fonction initialisation d'une nouvelle partie
    def new_game(self):
        window.fill(pygame.Color(0,0,0), screen)
        self.playing = True
    #Call Player class in Sprites
        self.player = Sprite(2, 1)

### Fonction récurente pour actualiser l'écran
    def draw_window(self):
        self.player.tiles.draw_map()

        # Load ALL Sprite at the very end ==> else : will not appear on screen
        window.blit(self.player.player_sprite, (self.player.x, self.player.y)).move_ip(self.player.x,self.player.y)
        print(self.player.x,self.player.y)
        if DEBUG:
            window.fill(pygame.color.Color(255,0,0), self.player.player_collider)
        # ___________________________________

    # Handle user input events
    def events(self):
        keys = pygame.key.get_pressed()
        #mouse_coord = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
        
        if not self.menu:
            if keys[pygame.K_ESCAPE]:
                image = pygame.image.load((img_path + 'mc_pausescreen' + '.png')).convert()
                image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
                self.menu = True
                window.blit(image, screen)
        if self.menu:
            if keys[pygame.K_SPACE]:
                self.menu = False

    # Update the game state based on user input and object behavior
    def update(self):
        self.player.update(self.COUNTER)
        if DEBUG:
            pygame.display.set_caption("Facing %s" % (self.player.player_facing))

    # Main game loop
    def run(self):
        if not self.playing:
            self.events()
            window.fill(pygame.color.Color(20,160,130))
            if start_button.check():
                self.playing = True
                self.init_game = True
            elif exit_button.check():
                self.running = False
                pass

        if self.init_game:
            self.new_game()
            self.init_game = False

        if self.playing:
            self.COUNTER += 1
    
            self.events()
            
            if not self.menu:
                self.draw_window()
                self.update()

        # Update display and tick clock
        clock.tick(FPS)
        pygame.display.update()

g = Game()
while g.running:
    g.run()

# Quit Pygame when the game loop exits
pygame.quit()