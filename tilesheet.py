from config import *
from levels import *

class Map:
# Chargement de la map à automatiser avec interface
    def __init__(self):
        self.background = []
        self.level = Levels('Forest')
        image = pygame.image.load((level_path + self.level.map + '/Preview/Background.png')).convert()
        self.image = pygame.transform.smoothscale(image, window.get_size())
        """for layer in (self.level.layer_founder()):
            image = pygame.image.load((level_path + self.level.map + '/layers/' + layer)).convert()
            self.background.append(image)"""
        self.ground = (SCREEN_HEIGHT // (1.36))


    def draw_map(self):
# Draw map's layers on screen
        window.fill(pygame.color.Color(0,0,0))
        width = self.image.get_width()
        window.blit(self.image, (0,0))

"""
        width = sky_img.get_width()
	    for x in range(5):
		    screen.blit(sky_img, ((x * width) - bg_scroll * 0.5, 0))
		    screen.blit(mountain_img, ((x * width) - bg_scroll * 0.6, SCREEN_HEIGHT - mountain_img.get_height() - 300))
		    screen.blit(pine1_img, ((x * width) - bg_scroll * 0.7, SCREEN_HEIGHT - pine1_img.get_height() - 150))
		    screen.blit(pine2_img, ((x * width) - bg_scroll * 0.8, SCREEN_HEIGHT - pine2_img.get_height()))
"""