import pygame 
from config import *


class Button():
	def __init__(self,x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.clicked = False

	def check(self):
		action = False
	#draw button
		window.blit(self.image, (self.rect.x, self.rect.y))

	#get mouse position
		pos = pygame.mouse.get_pos()
	#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == True and self.clicked == False:
				action = True
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == False:
			self.clicked = False

		return action