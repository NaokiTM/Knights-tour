import pygame
import sys
import random

def game(xSize, ySize):
  WIDTH, HEIGHT = xSize * 50, ySize * 50 #width and height in pixels, respectively
  BOARD_SIZE_X = xSize   #how many squares wide the board is 
  BOARD_SIZE_Y = ySize   #how many squares tall the board is 
  SQUARE_SIZE = WIDTH // BOARD_SIZE_X #could use HEIGHT // BOARD_SIZE_Y
  WHITE = pygame.Color("burlywood1")    #defines white macro
  BLACK = pygame.Color("chocolate4")    #define black as a macro 

      
  boardRows = 8                                                             #defined the board 
  boardCols = 8
  board = [[0 for y in range(boardCols)] for x in range(boardRows)]
 
  startPosX = random.randint(0, 7)                                         #initialises players position as a random place on board
  startPosY = random.randint(0, 7)
  playerPos = [startPosX, startPosY]

  pygame.init()                                                     #initialises pygame



  def takeInput():
    def get_square_clicked(mouse_x, mouse_y):
      row = mouse_y // SQUARE_SIZE
      col = mouse_x // SQUARE_SIZE
      return row, col
  
    for event in pygame.event.get(): #needed to define what an event class is 
      if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
        mouse_x, mouse_y = pygame.mouse.get_pos()
        clicked_square = get_square_clicked(mouse_x, mouse_y)
    
     
     
  def logic():

    #gives coordinates of possible moves, and each one contains the number of moves available from that possible move.
    knight_move_coords = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

    for moveset in knight_move_coords: #loops through the initial possible~moves 

      x1, y1 = playerPos[0] + moveset[0], playerPos[1] + moveset[1] #coordinates of a possible move are found
    
      if 0 <= x1 < BOARD_SIZE_X and 0 <= y1 < BOARD_SIZE_Y and playerPos[x1, y1] < 8: #checks if possible move is out of bounds porceeds if not
        possible_move = [x1, y1] #coordinates of possible move 

        for moveset in knight_move_coords: #loops through the outer moves from the possible move we are on.
            
            x2, y2 = possible_move[0] + moveset[0], possible_move[1] + moveset[1];  #coordinates of the outer move from the initial possible move

            if 0 <= x2 < BOARD_SIZE_X and 0 <= y2 < BOARD_SIZE_Y and playerPos[x2, y2] < 8:  #checks if second possible move is out of bounds
              possible_moves_count += 1 #adds 1 to the number of outer moves from the initial possible move, and goes on to try another possible move

      board[x1, y1] = possible_moves_count



    for event in pygame.event.get():
      if event.type == pygame.QUIT:       
          pygame.quit()
          sys.exit()
  
     
  def draw_board():  
    knight_image = pygame.image.load("knight.png") #import image of knight.png

    screen = pygame.display.set_mode((WIDTH, HEIGHT))    #sets screen as width x height pixels big
    pygame.display.set_caption("Chessboard")         

    for row in range(BOARD_SIZE_X):          
        for col in range(BOARD_SIZE_Y):         
            color = WHITE if (row + col) % 2 == 0 else BLACK       #white if even, black if odd
            pygame.draw.rect(
                screen,
                color,
                (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), #works cuz col and row start at 0
            )   #           x              y             width        height

    pygame.display.flip() #updates display


  while True:   
    takeInput()
    logic()
    draw_board() 
  

game(8,8) 




