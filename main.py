import pygame 
from pygame.locals import *

pygame.init()

screen_width = 800
screen_heigth = 800

screen = pygame.display.set_mode((screen_width,screen_heigth))
pygame.display.set_caption('TicTacToePython')

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()


