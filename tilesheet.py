from config import *
from levels import *

################################################################
#                                                              #
#                          Map Class                           #
#                                                              #
################################################################
class Map:
# Chargement de la map à automatiser avec interface
    def __init__(self):
        window.fill(pygame.color.Color(20,23,36))
        self.background = []
        self.level = Levels('Forest')
        image = pygame.image.load((level_path + self.level.map + '/Preview/Background.png')).convert()
        self.image = pygame.transform.smoothscale(image, screen.size)
        
        self.ground = GROUND_LEVEL
        self.memory = window.get_size()
        self.scroll = 0
        self.offset = math.ceil(SCREEN_WIDTH / self.image.get_width()) + 1
        window.blit(self.image, screen)
    
    def update(self):
        window.blit(self.image, screen)
        pygame.display.update(screen)

# SCROLL FUNC ==> Useless for now
"""    def scroll_map(self, x):
        i=0
        while(i < self.offset):
            window.blit(self.image, (self.image.get_width() * i + self.scroll, 0))
            
            i += 1
        # FRAME FOR SCROLLING
        self.scroll -= x * PLAYER_RUN
        # RESET THE SCROLL FRAME
        if abs(self.scroll) > self.image.get_width():
            self.scroll = 0

        pygame.display.update(screen)"""