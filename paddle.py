import pygame, random
import constants

class Paddle:
	def __init__(self, x, y):
		self.image = pygame.Surface([10, 95])
		self.image.fill(constants.WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.change_y = 0
		self.score = 0

	def update(self):
		self.rect.y += self.change_y
		if self.rect.bottom >= constants.screen_height:
			self.rect.bottom = constants.screen_height
		elif self.rect.y <= 0:
			self.rect.y = 0

