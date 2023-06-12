import pygame
pygame.init()
import newbutton
import sys
import random

#sudoku boardis 700x700 
# each big box is 233x233
# each small box is 77x77


w= 1200
h=800

#basics
screen = pygame.display.set_mode((w,h))
boardscreen = pygame.Surface([700,700], pygame.SRCALPHA, 32)
boardscreen = boardscreen.convert_alpha()
pygame.display.set_caption("SUDOKU")
screen.fill("cyan")


#fonts
titlefont= pygame.font.SysFont("Arial",70)
myfont= pygame.font.SysFont("Times",40)


#images
board_img = pygame.image.load("sudokuboard.jpg")

one_img = pygame.image.load("one.png").convert_alpha()
two_img = pygame.image.load("two.png").convert_alpha()
three_img = pygame.image.load("three.png").convert_alpha()
four_img = pygame.image.load("four.png").convert_alpha()
five_img = pygame.image.load("five.png").convert_alpha()
six_img = pygame.image.load("six.png").convert_alpha()
seven_img = pygame.image.load("seven.png").convert_alpha()
eight_img = pygame.image.load("eight.png").convert_alpha()
nine_img = pygame.image.load("nine.png").convert_alpha()

numbers_img=[one_img,two_img,three_img,four_img,five_img,six_img,seven_img,eight_img,nine_img]



#logics
run=True
logics={"showhome":True,"showmenu":False,"showgame":False,"xyz":True}


#fxns
def title(text,font,col,x,y):
   img = font.render(text,True,col)
   screen.blit(img,(x,y))

def myfunction():
   print("HELLO")

def newgamepressed():
   for key in logics:
      logics[key]=False
   logics["showgame"]=True

def board_filler():
   for i in range(9):
      for j in range(9):
         key=random.randint(0,8)
         print(key)
         boardscreen.blit(numbers_img[key],(78*i,78*j))
   
      




#screen

def menuscreen():
   screen.fill("pink")
   title("SUDOKU",titlefont,"red",500,10)
   for object in newbutton.all_buttons:
        object.process()

def homescreen():
   screen.fill("black")
   title("Welcome",titlefont,"red",500,10)
   title("To",titlefont,"red",500,110)
   title("Sudoku",titlefont,"red",500,210)
   title("Game",titlefont,"red",500,310)

   title("Made by Abhishek",myfont,"red",500,410)

   title("PRESS SPACE TO CONTINUE",titlefont,"red",100,700)

def gamescreen():
   screen.fill("black")
   screen.blit(board_img,(0,0))
   #screen.blit(one_img,(78,0))
   
   for i in range(9):
      for j in range(9):
         key=random.randint(0,8)
         print(key)
         screen.blit(numbers_img[key],(78*i,78*j))
   
   





#buttons
newgame_butt= newbutton.Button(screen,510,180,["red","blue","green"],200 ,50,newgamepressed,"New Game")
continuegame_butt= newbutton.Button(screen,510,280,["red","blue","green"],200 ,50,myfunction,"Continue")
settings_butt= newbutton.Button(screen,510,380,["red","blue","green"],200 ,50,myfunction,"Settings")
exit_butt= newbutton.Button(screen,510,480,["red","blue","green"],200 ,50,myfunction,"Exit")




while run==True:

   if logics["showhome"]==True:
      homescreen()
   if logics["showmenu"]==True:
      menuscreen()
   if logics["showgame"]==True:
      gamescreen()




   for event in pygame.event.get():
      if event.type==pygame.QUIT:
         run=False
      if event.type==pygame.KEYDOWN:
         if event.key==pygame.K_SPACE:
            for key in logics:
               logics[key] = False
               logics["showmenu"]=True
            
            
   
   
   
   pygame.display.update()
pygame.quit()


