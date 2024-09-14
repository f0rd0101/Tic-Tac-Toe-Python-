import pygame 
from pygame.locals import *

pygame.init()

screen_width = 300
screen_heigth = 300
line_width = 3
screen = pygame.display.set_mode((screen_width,screen_heigth))
pygame.display.set_caption('TicTacToePython')
markers = []
player = 1
clicked = False
winner = 0
game_over = False
black = (26,24,23)
white = (255,255,255)
font = pygame.font.SysFont(None,40)

rectangle_button = Rect(screen_width //2 - 80, screen_heigth //2, 160,50)




def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen,black,(x_pos * 100 + 15, y_pos * 100 + 15),(x_pos * 100 + 85, y_pos * 100 + 85),line_width)
                pygame.draw.line(screen,black,(x_pos * 100 + 15, y_pos * 100 + 85),(x_pos * 100 + 85, y_pos * 100 + 15),line_width)
            if y == -1:
                pygame.draw.circle(screen,white,(x_pos * 100 + 50, y_pos * 100 + 50),38,line_width)

            y_pos += 1
        x_pos += 1



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








def winning_check():
    global winner 
    global game_over

    y_pos = 0
    for x in markers:
        if sum(x) == 3:
            winner = 1
            game_over = True
        if sum(x) == -3:
            winner = 2
            game_over = True
        
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3:
            winner = 1
            game_over = True
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == -3:
            winner = 2
            game_over = True
        
        y_pos +=1


    if markers[0][0] + markers [1][1] + markers[2][2] == 3 or  markers[2][0] + markers [1][1] + markers[0][2] == 3:
        winner = 1
        game_over = True
                   
    if markers[0][0] + markers [1][1] + markers[2][2] == -3 or  markers[2][0] + markers [1][1] + markers[0][2] == -3:
        winner = 2
        game_over = True





def  show_winner(winner):
     win_text = 'Player ' + str(winner) + " wins!"
     win_img  = font.render(win_text,True, (222,214,214))
     pygame.draw.rect(screen,(57,54,54),(screen_width //2 - 100,screen_heigth //2 - 60, 200,50))
     screen.blit(win_img, (screen_width //2 - 100, screen_heigth //2 - 50))
     

     again_text = 'Play again?'
     again_img = font.render(again_text,True,(222,214,214))
     pygame.draw.rect(screen,(57,54,54),rectangle_button)
     screen.blit(again_img,(screen_width //2 - 80, screen_heigth //2 + 10))
     

run = True
while run:
    draw_grid()
    draw_markers()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if game_over == 0:
           if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
           if event.type == pygame.MOUSEBUTTONUP and clicked == True:
             clicked = False
             pos = pygame.mouse.get_pos()
             cell_x = pos[0]
             cell_y = pos[1]

             if markers[cell_x // 100][cell_y // 100] == 0:
                markers[cell_x // 100][cell_y // 100] = player
                player *= -1
                winning_check()

    if game_over == True:
       show_winner(winner)

       if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
           clicked = True
       if event.type == pygame.MOUSEBUTTONUP and clicked  == True:
           clicked = False
           pos = pygame.mouse.get_pos()
           if rectangle_button.collidepoint(pos):
               pos = [] 
               markers = []
               player = 1
               winner = 0
               game_over = False
               for x in range(3):
                   row = [0] *3
                   markers.append(row)
               
    pygame.display.update()
pygame.quit()


