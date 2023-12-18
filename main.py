import pygame
import sys
import random



def game(xSize, ySize):
  WIDTH, HEIGHT = xSize * 10, ySize * 10 #width and height in pixels, respectively
  BOARD_SIZE_X = xSize   #how many squares wide the board is 
  BOARD_SIZE_Y = ySize   #how many squares tall the board is 
  SQUARE_SIZE = WIDTH // BOARD_SIZE_X #could use HEIGHT // BOARD_SIZE_Y
  WHITE = pygame.Color("burlywood1")    #defines white macro
  BLACK = pygame.Color("chocolate4")    #define black as a macro 

      
  boardRows = 8                                                             #defined the board 
  boardCols = 8
  chessBoard = [[0 for y in range(boardCols)] for x in range(boardRows)]

 
  startPosX = random.randint(0, 7)                                         #initialises players position as a random place on board
  startPosY = random.randint(0, 7)
  playerPos = [startPosX, startPosY]

  pygame.init()
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  pygame.display.set_caption("Chessboard")





  def takeInput():


    def get_square_clicked(mouse_x, mouse_y):
      row = mouse_y // SQUARE_SIZE
      col = mouse_x // SQUARE_SIZE
      return row, col
    

    for event in pygame.event.get(): import pygame
import sys
import random



def game(xSize, ySize):
  WIDTH, HEIGHT = xSize * 10, ySize * 10 #width and height in pixels, respectively
  BOARD_SIZE_X = xSize   #how many squares wide the board is 
  BOARD_SIZE_Y = ySize   #how many squares tall the board is 
  SQUARE_SIZE = WIDTH // BOARD_SIZE_X #could use HEIGHT // BOARD_SIZE_Y
  WHITE = pygame.Color("burlywood1")    #defines white macro
  BLACK = pygame.Color("chocolate4")    #define black as a macro 

      
  boardRows = 8                                                             #defined the board 
  boardCols = 8
  chessBoard = [[0 for y in range(boardCols)] for x in range(boardRows)]

 
  startPosX = random.randint(0, 7)                                         #initialises players position as a random place on board
  startPosY = random.randint(0, 7)
  playerPos = [startPosX, startPosY]

  pygame.init()
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  pygame.display.set_caption("Chessboard")




  def takeInput():


    def get_square_clicked(mouse_x, mouse_y):
      row = mouse_y // SQUARE_SIZE
      col = mouse_x // SQUARE_SIZE
      return row, col
    

    for event in pygame.event.get(): 
      if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
        mouse_x, mouse_y = pygame.mouse.get_pos() 
        clicked_square = get_square_clicked(mouse_x, mouse_y)

        squarePosX, squarePosY = clicked_square

        playerPos[0], playerPos[1] = squarePosX, squarePosY

    
    
     


     
  def logic():

    #gives coordinates of possible moves, and each one contains the number of moves available from that possible move.#
    knight_move_coords = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

    # playerPos[x1, y1] < 8: 
    for moveset in knight_move_coords: #runs through possible moves from playerPos
      possible_moves_count = 0;
      x1, y1 = playerPos[0] + moveset[0], playerPos[1] + moveset[1] 
      if 0 <= x1 < BOARD_SIZE_X and 0 <= y1 < BOARD_SIZE_Y:
        possible_move = [x1, y1] 


        for moveset in knight_move_coords: #counts outer moves from each possible move
          x2, y2 = possible_move[0] + moveset[0], possible_move[1] + moveset[1];  
          if 0 <= x2 < BOARD_SIZE_X and 0 <= y2 < BOARD_SIZE_Y: 
            possible_moves_count += 1  

          chessBoard[x1][y1] = possible_moves_count






     
  def draw_board():  
    knight_image_big = pygame.image.load("knight.png") #import image of knight.png
    knight_image = pygame.transform.scale(knight_image_big, (SQUARE_SIZE, SQUARE_SIZE))
    font = pygame.font.Font(None, SQUARE_SIZE - 5)



    for x in range(BOARD_SIZE_X):          
        for y in range(BOARD_SIZE_Y):         
            color = WHITE if (x + y) % 2 == 0 else BLACK       #white if even, black if odd
            pygame.draw.rect(
                screen,
                color,
                (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), #works cuz col and row start at 0
            )   #           x              y             width        




            
            if playerPos[0] == x and playerPos[1] == y: #has the if statement to only print the knight where playerPos is.
              screen.blit(knight_image, (x * SQUARE_SIZE, y * SQUARE_SIZE))


            #draw number of possible moves onto screen
            if chessBoard[x][y] <= 0:
              keepPrintingScreenHereUntilRestartGame = 0
            elif chessBoard[x][y] > 0:
              num = chessBoard[x][y]
              num_text = str(num)

              render_num = font.render(num_text, True, (0,0,0))
              screen.blit(render_num, ((x * SQUARE_SIZE) + SQUARE_SIZE / 2, (y * SQUARE_SIZE) + SQUARE_SIZE / 2))

    pygame.display.flip() 





  while True: 
    for event in pygame.event.get():
      if event.type == pygame.QUIT:       
          pygame.quit()
          sys.exit() 
    takeInput()
    logic()
    draw_board() 
  


game(8,8) 


