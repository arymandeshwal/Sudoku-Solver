import pygame
pygame.init()

winX,winY = 370,370
win = pygame.display.set_mode((winX,winY))
pygame.display.set_caption('Sudoku Solver')
##win.fill((235,238,209))

board = [
        [8,0,2,7,0,0,4,0,0],
        [0,1,0,0,0,9,0,0,5],
        [0,4,0,0,8,0,2,0,0],
        [0,0,0,0,5,0,9,2,0],
        [0,0,0,8,0,7,0,0,6],
        [7,0,9,0,6,0,0,5,0],
        [0,0,3,0,0,5,7,0,9],
        [6,0,0,0,1,0,3,0,0],
        [4,0,0,2,0,0,0,0,8]
        ]

def write(X,Y,num):
    green = (0, 255, 0) 
    blue = (0, 0, 128) 
    font = pygame.font.Font('freesansbold.ttf', 25)
    text = font.render(num, True, green, (255,255,255))
    textRect = text.get_rect()
    textRect.topleft = (X+7,Y+2)
    win.blit(text, textRect)

def draw_grid():
    x =10
    y =10
    height = 30
    width = 30
    #lines
    pygame.draw.line(win,(255,0,0),(125,0),(125,winY),5)
    pygame.draw.line(win,(255,0,0),(245,0),(245,winY),5)
    pygame.draw.line(win,(255,0,0),(0,125),(winX,125),5)
    pygame.draw.line(win,(255,0,0),(0,245),(winX,245),5)
    #grid
    for i in range(0,9):
        for j in range(0,9):
            X,Y = x + (width+x)*j,y+(height+y)*i
            pygame.draw.rect(win, (255,255,255),(X,Y,width,height))
            if board[i][j] == 0:
                text = ' '
            else:
                text = str(board[i][j])
            write(X,Y,text)
        

def main():
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_grid()
    ##    write(50,50)
        
        pygame.display.update()

    pygame.quit()
main()
