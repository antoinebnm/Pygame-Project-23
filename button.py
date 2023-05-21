import pygame 
from config import *

################################################################
#                                                              #
#   		   Buttons Management System Class   			   #
#                                                              #
################################################################
class Button():
	def __init__(self,x, y, image, scale=1):

		# Check if button is an Image or just a Rectangle to control
		if type(image) == pygame.rect.Rect:
			self.image = image
			self.rect = image

			self.rect.topleft = (x, y)
		else:
			width = image.get_width()
			height = image.get_height()
			self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
			self.rect = self.image.get_rect()

			self.rect.center = (x, y)
		
		self.clicked = False

# Print Button/ Rect on Screen and check if User Clicked on it
	def check(self):
		action = False
	#draw button
		if type(self.image) == pygame.rect.Rect:
			pass
		else:
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