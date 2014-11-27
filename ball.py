import pygame, sys, random
import constants

class Ball:
	def __init__(self, x, y):
		self.image = pygame.Surface([10, 10])
		self.image.fill(constants.WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.change_x = random.choice([-8, 8])
		self.change_y = random.choice([-8, 8])

	def update(self):
		self.rect.x += self.change_x
		for paddle in self.paddle_list:
			if self.rect.colliderect(paddle.rect):
				self.change_x *= -1
		'''		
		if self.rect.x >= constants.screen_width or self.rect.right <= 0:
			if self.change_x < 0:
				self.paddle_list[1].score += 1
			else:
				self.paddle_list[0].score += 1
			if self.paddle_list[0].score >= 3 or self.paddle_list[1].score >= 3:
				pygame.quit()
				sys.exit()
			else:
				self.rect.x = constants.screen_width/2
				self.rect.y = constants.screen_height/2
		'''		
		self.rect.y += self.change_y
		if self.rect.bottom >= constants.screen_height or self.rect.y <= 0:
			self.change_y *= -1

