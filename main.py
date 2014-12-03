# Programmed by Nathan Yong
import pygame, sys, random
import constants
import text_functions
from pygame.locals import *
from paddle import Paddle
from ball import Ball
from score import Score
pygame.init()

screen = pygame.display.set_mode((constants.screen_width, constants.screen_height))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()

ball = Ball(random.randint(0, 800), random.randint(0, 600))

paddle1 = Paddle(10, constants.screen_height/2)
paddle2 = Paddle(780, constants.screen_height/2)

paddle_list = [paddle1, paddle2]

ball.paddle_list = paddle_list

scoreBoard = Score(constants.screen_width/2, 0)

def terminate():
	pygame.quit()
	sys.exit()

while True:
	# Fill the screen
	screen.fill(constants.BLACK)

	# Display the game objects
	for paddle in paddle_list:
		screen.blit(paddle.image, (paddle.rect.x, paddle.rect.y))
	screen.blit(ball.image, (ball.rect.x, ball.rect.y))

	# Display the score board
	screen.blit(scoreBoard.text, scoreBoard.rect)
	
	# Game events
	for event in pygame.event.get():
		if event.type == QUIT:
			terminate()
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				terminate()
			elif event.key == K_w:
				paddle1.change_y -= 6
			elif event.key == K_s:
				paddle1.change_y += 6
			elif event.key == K_UP:
				paddle2.change_y -= 6
			elif event.key == K_DOWN:
				paddle2.change_y += 6
		elif event.type == KEYUP:
			if event.key == K_w:
				paddle1.change_y += 6
			elif event.key == K_s:
				paddle1.change_y -= 6
			elif event.key == K_UP:
				paddle2.change_y += 6
			elif event.key == K_DOWN:
				paddle2.change_y -= 6

	# Updates the game objects
	for paddle in paddle_list:
		paddle.update()
	ball.update()
	if ball.rect.right >= constants.screen_width or ball.rect.x <= 0:
		if ball.change_x >= 0:
			paddle1.score += 1
		else:
			paddle2.score += 1
		ball.change_x = 6
		ball.change_y = 6
		ball.rect.topleft = (random.randint(0, 800), random.randint(0, 600))
		if paddle1.score >= 10 or paddle2.score >= 10:
			scoreBoard.update(str(paddle1.score) + " | " + str(paddle2.score))
			text_functions.showText("Game Over", (constants.screen_width/2, constants.screen_height/2), screen)
			pygame.time.wait(500)
			pygame.display.update()
			terminate()
	scoreBoard.update(str(paddle1.score) + " | " + str(paddle2.score))
	pygame.display.update()
	clock.tick(constants.fps)
