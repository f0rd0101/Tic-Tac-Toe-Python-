import pygame 
from pygame.locals import *

pygame.init()

screen_width = 300
screen_heigth = 300
line_width = 3
screen = pygame.display.set_mode((screen_width,screen_heigth))
pygame.display.set_caption('TicTacToePython')
markers = []
 
def draw_grid():
    grid_color = (255,255,204)
    background_color = (204, 153, 102)
    screen.fill(background_color)
    for x in range(1,3):
        pygame.draw.line(screen,grid_color,(0,x * 100), (screen_width, x * 100), line_width)
        pygame.draw.line(screen,grid_color,(x * 100, 0), (x * 100, screen_heigth), line_width)


for x in range(3):
    row = [0] * 3
    markers.append(row)


run = True
while run:
    draw_grid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()


