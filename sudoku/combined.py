import pygame
import sys

pygame.init()

winX,winY = 370,370
win = pygame.display.set_mode((winX,winY))
pygame.display.set_caption('Sudoku Solver')
##win.fill((235,238,209))

##algoithm

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

##def board_print(board):
##    for i in range(len(board)):
##        if i%3==0 and i != 0:
##            print('---------------------')
##        for j in range(len(board[0])):
##            if j%3 ==0  and j!=0:
##                print('| ',end='')
##            print(board[i][j],end=' ')
##
##        print()

def find (board):
    for i in range(len(board)):
        for j in range(len(board[0])):
           if board[i][j] == 0 :
               return (i,j) # pos of i
    return None

def validate(board,num,pos):
    for i in range(len(board)):
        if board[pos[0]][i] == num and pos[1]!= i :
            return False

    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0]!= i:
            return False
    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3 , box_y*3 +3):
        for j in range(box_x*3 , box_x*3 +3):
            if board[i][j] == num and (i,j) != pos:
                return False
        
    return True

def solve(board):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    draw_grid()
    pygame.display.update()
    
    x = find(board)
    if not x:
        return True

    else:
        row,col = x

    for i in range(1,10):
        if validate(board,i,(row,col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False



##board_print(board)
##solve(board)
##print('_______________________________________________')
##board_print(board)



##GUI
def write(X,Y,num):
    green = (0, 255, 0) 
    blue = (0, 0, 128) 
    font = pygame.font.Font('freesansbold.ttf', 25)
    text = font.render(num, True, green, (255,255,255))
    textRect = text.get_rect()
    textRect.topleft = (X+7,Y+2)
    win.blit(text, textRect)

def draw_grid():
    pygame.time.delay(50)
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
   

solve(board)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
