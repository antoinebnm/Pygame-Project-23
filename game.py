###################################################################
#                                                                 #
#                  Imports and images loading                     #
#                                                                 #
###################################################################

from sprites import *
from fight import *
from button import *

# Button images
newg_img = pygame.image.load(img_path + 'new-game_btn.png').convert_alpha()
load_img = pygame.image.load(img_path + 'load_btn.png').convert_alpha()
option_img = pygame.image.load(img_path + 'settings_btn.png').convert_alpha()
exit_img = pygame.image.load(img_path + 'exit_btn.png').convert_alpha()
menu_img = pygame.image.load((img_path + 'mc_pausescreen' + '.png')).convert_alpha()

# Monsters Images
ogre = pygame.image.load((sprite_path + 'Ogre' + '.png')).convert_alpha()
dragon = pygame.image.load((sprite_path + 'Dragon' + '.png')).convert_alpha()


###################################################################
#                                                                 #
#                         Main Game Class                         #
#                                                                 #
###################################################################
# Screen And User Interface Management
class Game: 
    def __init__(self):
        # Initialize Pygame and game objects
        pygame.init()

    # Class Variables
        window.fill(pygame.Color(0,0,0)) # Add a load screen maybe ?
        self.menu = False
        self.playing = False
        self.running = True
        self.init_game = False
        self.fighting = False

    # Buttons for UI
        self.ind = newg_img.get_height() + 20
        self.newg_button = Button(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) + self.ind*0, newg_img, 0.6)
        self.load_button = Button(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) + self.ind*0.5, load_img, 0.6)
        self.option_button = Button(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) + self.ind*1, option_img, 0.6)
        self.exit_button = Button(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) + self.ind*1.5, exit_img, 0.6)
        self.rect_return = Button(301,207,pygame.Rect(301,207,550,60))
        self.rect_quit = Button(301,351,pygame.Rect(301,351,550,60))
        self.rect_settings = Button(301,380,pygame.Rect(301,280,263,60))
        self.rect_stats = Button(588,280,pygame.Rect(588,280,263,60))

### New game init function
    def new_game(self):
        self.ind = 0

    # Reset datas
        """ To do """
        FightSyst.wave_num = 0
        self.playing = True
    #Call Player class in Sprites (print and manage sprites + map)
        self.player = Sprite(1)
    # Init screen
        window.fill(COLOR_UI)
        window.blit(self.player.tiles.image,screen)
        ui_update()


    ###################################################################
    #                                                                 #
    #                        Events Management                        #
    #                                                                 #
    ###################################################################
    def events(self):
        global mouse_coord
        keys = pygame.key.get_pressed()
        mouse_coord = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                raise SystemExit

            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode(event.dict['size'], pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
                
                if self.playing and not self.menu:
                    image = self.player.tiles.image
                    screen.blit(pygame.transform.scale(image, event.dict['size']), (0, 0))
                if not self.playing:
                    window.fill(COLOR_MENU)
                    size = [round(event.dict['size'][0] / 1120, 2), round(event.dict['size'][1] / 620, 2)]
                    size = size[0] * size[1]
                    self.ind = size * newg_img.get_height() + size * 20
                    
                    self.newg_button = Button(event.dict['size'][0] // 2, event.dict['size'][1] // 2 + self.ind*0, newg_img, size * 0.6)
                    self.load_button = Button(event.dict['size'][0] // 2, event.dict['size'][1] // 2 + self.ind*0.5, load_img, size * 0.6)
                    self.option_button = Button(event.dict['size'][0] // 2, event.dict['size'][1] // 2 + self.ind*1, option_img, size * 0.6)
                    self.exit_button = Button(event.dict['size'][0] // 2, event.dict['size'][1] // 2 + self.ind*1.5, exit_img, size * 0.6)
                if self.menu:
                    image = menu_img
                    screen.blit(pygame.transform.scale(image, event.dict['size']), (0, 0))

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
            if self.rect_return.check():
                self.menu = False
                self.player.tiles.update()
                self.update()
            elif self.rect_quit.check():
                self.running = False
                pygame.quit()
                raise SystemExit
            if keys[pygame.K_k]:
                for x in player_group:
                    x.is_alive = False


    # Update the game state based on user input and object behavior
    def update(self):
        if self.playing:
            self.player.update()

            for i,monster in enumerate(Waves[FightSyst.wave_num]):
                if monster.is_alive:
                    if monster == Ogre:
                        exec(f'window.blit({(monster.char_name).lower()},(screen.right - 120 - ({i}*30), self.player.tiles.ground - 18))')
                    else:
                        exec(f'window.blit({(monster.char_name).lower()},(screen.right - 160 - ({i}*30), self.player.tiles.ground - 30))')
            
            ui_update()


    ###################################################################
    #                                                                 #
    #                          Main Game Loop                         #
    #                                                                 #
    ###################################################################
    def run(self):
        global mouse_coord
    # IF for Introduction Screen Menu
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
    
    # IF for game init
        if self.init_game:
            self.new_game()
            self.init_game = False

    # IF for the game loop, with events and screen update management
        if self.playing:
            self.events()
            self.update() if not self.menu else None

        # Threading of the Fight Core, dual task in parallel
            if not FightSyst.ThreadLaunched:
                if FightSyst.wave_num in range(len(Waves)) and not FightSyst.fighting and not FightSyst.gameover:
                    # Daemon = True : so Thread closes when main pygame loop stops
                    fight_thread = threading.Thread(target=FightSyst.main, daemon=True, args=[FightSyst.wave_num], name="FightSystem")
                else:
                    fight_thread = threading.Thread(target=FightSyst.end_game, daemon=True, name="FightEnd")

                fight_thread.start()
                FightSyst.ThreadLaunched = True
                
                if fight_thread.name == 'FightEnd':
                    self.playing = False
            
                

        if DEBUG:
            pygame.display.set_caption(f"Mouse Coords: x:{mouse_coord[0]} | y:{mouse_coord[1]}")

        # Update display and tick clock
        clock.tick(FPS)
        pygame.display.update()