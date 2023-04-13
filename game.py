from tilesheet import *
from levels import *
from sprites import *
from config import *
from button import *

#button images
newg_img = pygame.image.load(img_path + 'new-game_btn.png').convert()
load_img = pygame.image.load(img_path + 'load_btn.png').convert()
option_img = pygame.image.load(img_path + 'settings_btn.png').convert()
exit_img = pygame.image.load(img_path + 'exit_btn.png').convert()
ind = newg_img.get_height() + 20
newg_button = Button(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2), newg_img, 0.6)
load_button = Button(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) + ind*0.5, load_img, 0.6)
option_button = Button(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) + ind, option_img, 0.6)
exit_button = Button(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) + ind*1.5, exit_img, 0.6)

class Game:
    def __init__(self):
        # Initialize Pygame and game objects
        pygame.init()
        
        window.fill(pygame.Color(0,0,0)) # Add load screen
        self.menu = False
        self.playing = False
        self.running = True
        self.COUNTER = 0
        self.init_game = False

### Fonction initialisation d'une nouvelle partie
    def new_game(self):
    # Reset datas
        """ To do """
        self.playing = True
    #Call Player class in Sprites
        self.player = Sprite(2, 1)
    # Init screen
        window.fill(COLOR_UI)
        window.blit(self.player.tiles.image,screen)

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
                window.blit(image, window)
        if self.menu:
            if keys[pygame.K_SPACE]:
                self.menu = False

    # Update the game state based on user input and object behavior
    def update(self):
        for character in PLAYER_CHARACTERS:
            i = PLAYER_CHARACTERS.index(character)
            window.blit(self.player.team_sprites[i], (self.player.x + (i*30), self.player.y))
        self.player.update(self.COUNTER)
        self.player.tiles.update(self.COUNTER)

    # Main game loop
    def run(self):
        if not self.playing:
            self.events()
            window.fill(pygame.color.Color(20,160,130))
            if newg_button.check():
                self.playing = True
                self.init_game = True
            elif load_button.check():
                pass
            elif option_button.check():
                pass
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
                self.update()
    
        if DEBUG:
            window.fill(pygame.color.Color(255,0,0), self.player.player_collider)
            pygame.display.set_caption("Facing %s" % (self.player.player_facing))

        # Update display and tick clock
        clock.tick(FPS)
        pygame.display.update()