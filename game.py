from sprites import *
from fight import *
from button import *

#button images
newg_img = pygame.image.load(img_path + 'new-game_btn.png').convert_alpha()
load_img = pygame.image.load(img_path + 'load_btn.png').convert_alpha()
option_img = pygame.image.load(img_path + 'settings_btn.png').convert_alpha()
exit_img = pygame.image.load(img_path + 'exit_btn.png').convert_alpha()
menu_img = pygame.image.load((img_path + 'mc_pausescreen' + '.png')).convert_alpha()


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

        self.ind = newg_img.get_height() + 20
        self.newg_button = Button(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) + self.ind*0, newg_img, 0.6)
        self.load_button = Button(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) + self.ind*0.5, load_img, 0.6)
        self.option_button = Button(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) + self.ind*1, option_img, 0.6)
        self.exit_button = Button(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) + self.ind*1.5, exit_img, 0.6)

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
        text_update()


    # Handle user input events
    def events(self):
        keys = pygame.key.get_pressed()
        #mouse_coord = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode(
                event.dict['size'], pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
                
                if self.playing and not self.menu:
                    if self.playing:
                        image = self.player.tiles.image
                    elif self.menu:
                        image = menu_img
                    screen.blit(pygame.transform.scale(image, event.dict['size']), (0, 0))
                elif not self.playing:
                    window.fill(COLOR_MENU)
                    size = [round(event.dict['size'][0] / 1120, 2), round(event.dict['size'][1] / 620, 2)]
                    size = size[0] * size[1]
                    self.ind = size * newg_img.get_height() + size * 20
                    
                    self.newg_button = Button(event.dict['size'][0] // 2, event.dict['size'][1] // 2 + self.ind*0, newg_img, size * 0.6)
                    self.load_button = Button(event.dict['size'][0] // 2, event.dict['size'][1] // 2 + self.ind*0.5, load_img, size * 0.6)
                    self.option_button = Button(event.dict['size'][0] // 2, event.dict['size'][1] // 2 + self.ind*1, option_img, size * 0.6)
                    self.exit_button = Button(event.dict['size'][0] // 2, event.dict['size'][1] // 2 + self.ind*1.5, exit_img, size * 0.6)
                elif self.menu:
                    screen.blit(pygame.transform.scale(menu_bg, event.dict['size']), (0, 0))

                pygame.display.flip()

        if not self.menu:
            menubg = False
            if keys[pygame.K_ESCAPE]:
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


    # Update the game state based on user input and object behavior
    def update(self):
        self.player.update(self.COUNTER)
        text_update()

    # Main game loop
    def run(self):
        if not self.playing:
            self.events()
            window.fill(COLOR_MENU)
            if self.newg_button.check():
                self.playing = True
                self.init_game = True
            elif self.load_button.check():
                pass
            elif self.option_button.check():
                pass
            elif self.exit_button.check():
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
    
        """if DEBUG:
            window.fill(pygame.color.Color(255,0,0), self.player.player_collider)
            pygame.display.set_caption("Facing %s" % (self.player.player_facing))
"""
        # Update display and tick clock
        clock.tick(FPS)
        pygame.display.update()