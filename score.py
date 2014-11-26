import pygame
import constants
pygame.init()

fontObj = pygame.font.Font("font.ttf", 32)

class Score:
	def __init__(self, centerx, y):
		self.text = fontObj.render("0 | 0", True, constants.WHITE)
		self.rect = self.text.get_rect()
		self.rect.centerx = centerx
		self.rect.y = y

	def update(self, text):
		self.text = fontObj.render(text, True, constants.WHITE)
