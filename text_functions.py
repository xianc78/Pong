import pygame.font
import constants
pygame.font.init()

fontObj = pygame.font.Font("font.ttf", 16)

def showText(text, pos, screen):
    textObj = fontObj.render(text, True, constants.WHITE)
    textRect = textObj.get_rect()
    textRect.center = pos
    screen.blit(textObj, textRect)
