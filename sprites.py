from tilesheet import *


################################################################
#                                                              #
#             Sprites Class / Characters Management            #
#                                                              #
################################################################
class Sprite():
    def __init__(self, scale):
        self.sprite_animation = 'stand'
        self.num_tileset = [0,0,0,0]

        self.w = TILE_SIZE
        self.h = TILE_SIZE

        self.scale = scale

    #   Need to call Tilesheet here 'cause of the colliders check
        self.tiles = Map()

# Var de position x, y du joueur
        self.player_facing = 'right'
        self.sprite_frame = 1
        self.facing_sprite = 12

        if MAP_VIEW:
            self.x = SCREEN_WIDTH // 400
            self.y = self.tiles.ground
        elif MAP_VIEW:
            self.x = SCREEN_WIDTH // 30
            self.y = SCREEN_HEIGHT // 2

        self.assign_sprite_tileset()
        
        if DEBUG:
            if MAP_VIEW == 2.5:
                self.player_collider = pygame.rect.Rect(self.team_sprites.get_rect(topleft=(self.x + 16, self.y + 48), width=24, height=16))


# Chargement tileset du chararcter / à automatiser avec interface
    def assign_sprite_tileset(self):
    # PLAYERCHAR = warrior, archer, mage, healer
        self.team_sprites = []
        self.sprites_tilesets = []
        for character in PLAYER_CHARACTERS.keys():
            i = self.num_tileset[list(PLAYER_CHARACTERS.keys()).index(character)]
        # sprites_tilesets = all sprites tilesets | team_sprites = all sprites frames
            self.sprites_tilesets.append(self.load_tileset((character + '_' + str(self.num_tileset[i]) + '.png')))
            self.team_sprites.append(self.get_sprite(character, self.sprite_frame, self.facing_sprite))
            """ Add indexes to scale player """
            self.team_sprites[i] = pygame.transform.scale(self.team_sprites[i], (((int(self.team_sprites[i].get_width())*self.scale)),(int(self.team_sprites[i].get_height())*self.scale)))

# Suite du chargement et mise en variable
    def load_tileset(self, filename, rows = 21, cols = 13):
        image = pygame.image.load((sprite_path + filename)).convert() # Save des perfs, add .convert()
        self.sprite_table = []
        for tile_x in range(0, cols):
            line = []
            self.sprite_table.append(line)
            for tile_y in range(0, rows):
                rect = (tile_x * SPRITE_SIZE, tile_y * SPRITE_SIZE, SPRITE_SIZE, SPRITE_SIZE) # tiles x&y * 2 ==> TILE_SIZE * 2 = SPRITE_SIZE
                line.append(image.subsurface(rect))
        return self.sprite_table
    
# Fonction de récup. de tile, tout est dans le nom
    def get_sprite(self, table_name, x_char=1, y_char=12):
        i = list(PLAYER_CHARACTERS.keys()).index(table_name)
        return self.sprites_tilesets[i][x_char - 1][y_char - 1]

# Dessiner le character sur l'écran (.blit)
    def draw_sprite(self,x,y):
        memory = []
        for character in PLAYER_CHARACTERS.keys():
            i = list(PLAYER_CHARACTERS.keys()).index(character)
            memory.append(self.get_sprite(character, self.sprite_frame, self.facing_sprite))
            window.blit(self.team_sprites[i], (self.x + 90 - (i*30), self.y))

        if DEBUG:
            if MAP_VIEW == 2.5:
                self.player_collider = self.team_sprites.get_rect(topleft=(x + 16, y + 48), width=24, height=16)

# FONCTION UPDATE / récurrence
    def update(self):
        self.movements()
        self.animation()
# redraw du sprite après check de l'animation
        self.draw_sprite(self.x,self.y)

    def animation(self):
        if self.sprite_animation == 'walk':
            if self.player_facing == 'left':
                self.facing_sprite = 10
            elif self.player_facing == 'right':
                self.facing_sprite = 12

        keys = pygame.key.get_pressed()

        if (keys[PLAYER_LEFT_KEY] or keys[PLAYER_RIGHT_KEY]):
            self.sprite_animation = 'walk'
        else:
            self.sprite_animation = 'stand'

        self.animate_frames()

    def animate_frames(self):
        if self.sprite_animation == 'walk':
            if (self.sprite_frame < 9):
                pass # DO CLOCK
                #if ((pygame % 6)==0):
                #    self.sprite_frame += 1
            else:
                self.sprite_frame = 1
        if self.sprite_animation == 'stand':
            self.sprite_frame = 1

# Useless on 2D Map --> For 2.5 Map
    def movements(self):
        keys = pygame.key.get_pressed()
        pass