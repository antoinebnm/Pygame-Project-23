from sprites import *
#from fight import *
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
menu_img = pygame.image.load((img_path + 'mc_pausescreen' + '.png')).convert()


class Game:
    def __init__(self):
        # Initialize Pygame and game objects
        pygame.init()
        
        window.fill(pygame.Color(0,0,0)) # Add load screen
        self.text_box = pygame.rect.Rect((0,0),(screen.size))
        self.menu = False
        self.playing = False
        self.running = True
        self.COUNTER = 0
        self.init_game = False

### Fonction initialisation d'une nouvelle partie
    def new_game(self):
    # Reset datas
        """ To do """
        self.wave_num = 0
        self.playing = True
    #Call Player class in Sprites
        self.player = Sprite(1)
    # Init screen
        window.fill(COLOR_UI)
        window.blit(self.player.tiles.image,screen)
        self.text_update()


    # Handle user input events
    def events(self):
        keys = pygame.key.get_pressed()
        #mouse_coord = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()

        if not self.menu:
            menubg = False
            if keys[pygame.K_ESCAPE]:
                #pygame.quit()
                self.menu = True
                if not menubg:
                    menubg = True
                    menu_bg = pygame.transform.smoothscale(menu_img, window.get_size())
                    window.blit(menu_bg,window.get_rect())
        if self.menu:
            if keys[pygame.K_SPACE]:
                self.menu = False
                self.player.tiles.scroll_map(0)
                self.update()
 
    def text_update(self):
        ui = pygame.rect.Rect(screen.left, screen.bottom, window.get_width(), LOWER_MARGIN)
        window.fill(COLOR_UI,ui)
    # UI indicator
        self.text_write(100,20, 'Health points :')
        self.text_write(100,40, 'Ammo :')
        self.text_write(700,20, 'Current Attacker :')
        self.text_write(700,40, 'Next Attacker :')
    # Wave indicator
        self.text_write(400,((-1) * SCREEN_HEIGHT + 60), ('Wave n°' + str(self.wave_num)),2.4)

    def text_write(self, x, y, text='default text', scale=1):
        scale = float(scale)
        text = font.render(text, False, COLOR_WHITE).convert_alpha()
        text = pygame.transform.scale_by(text,scale)
        text_rect = text.get_rect()
        y += SCREEN_HEIGHT # adjust to bottom of screen / ui
        text_rect.topleft = ((x),(y))
        window.blit(text, text_rect)

    # Update the game state based on user input and object behavior
    def update(self):
        self.player.update(self.COUNTER)
        self.player.tiles.update(self.COUNTER)
        self.text_update()

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