import pygame
from pygame.locals import *

import newbutton
import sys
import random
import sudokumaker
import dragndrop

pygame.init()

#sudoku boardis 700x700 
# each big box is 233x233
# each small box is 77x77


w= 1200
h=800

#basics
screen = pygame.display.set_mode((w,h))
boardscreen = pygame.Surface([700,700])
boardscreen = boardscreen.convert_alpha()
pygame.display.set_caption("SUDOKU")
screen.fill("cyan")

#logics
run=True
logics={"showhome":True,"showmenu":False,"showgame":False,"showlevel":False}
difficulty="hard"


clock = pygame.time.Clock()
timer_value=0
timer_started=False


#sudokumaker

finalgrid=sudokumaker.generatepuzzle(difficulty)

empty_coordinates = []
empty_rect =[]
filled_rect=[]

for i in range(9):
   for j in range(9):
      if finalgrid[i][j]==0:
         empty_coordinates.append(((78*i),(j*78)))
wow=0
for x,y in empty_coordinates:
   empty_rect.append(pygame.Rect(x,y,78,78))
   wow+=1






  





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
redbox_img = pygame.image.load("redbox.png").convert_alpha()
# greenbox_img = pygame.image.load("greenbox.png").convert_alpha()
blank_img = pygame.image.load("blank.png").convert_alpha()
redbox_img= pygame.transform.scale(redbox_img,(75,75))


numbers_img=[blank_img,one_img,two_img,three_img,four_img,five_img,six_img,seven_img,eight_img,nine_img]

bar_img = pygame.image.load("emptybar.jpg")


#draggers
dragger = [0]*10
for i in range(1,10):
   dragger[i] = dragndrop.DragnDrop(screen,numbers_img[i],(78*(i-1)),722)










#fxns
def title(text,font,col,x,y):
   img = font.render(text,True,col)
   screen.blit(img,(x,y))

def myfunction():
   print("HELLO")

def newgamepressed():
   logics["showgame"]=False
   logics["showmenu"]=False
   logics["showlevel"]=True
   pygame.time.delay(100)

def newbox_printer():
   
   if red:
      screen.blit(redbox_img,(x,y))
   for a,b in filled_rect:
      screen.blit(numbers_img[a],b)

def draw_timer(time):
   timer_text = myfont.render("TIME: " + str(time),True,"white")
   screen.blit(timer_text,(800,20))

def easypress():
   difficulty="easy"
   logics["showlevel"]=False
   logics["showgame"]=True
   
def mediumpress():
   difficulty="medium"
   logics["showlevel"]=False
   logics["showgame"]=True
   
def hardpress():
   difficulty="hard"
   logics["showlevel"]=False
   logics["showgame"]=True
   
def godmodepress():
   logics["showgame"]=True
   logics["showlevel"]=False
   difficulty="hard"


#def correctornot(num):




      




#screen

def menuscreen():
   screen.fill("pink")
   title("SUDOKU", titlefont, "red", 500, 10)

   for button in menu_buttons:
      button.process()

def homescreen():
   screen.fill("black")
   title("Welcome",titlefont,"red",500,10)
   title("To",titlefont,"red",500,110)
   title("Sudoku",titlefont,"red",500,210)
   title("Game",titlefont,"red",500,310)

   title("Made by Abhishek",myfont,"red",500,410)

   title("PRESS SPACE TO CONTINUE",titlefont,"red",100,700)
   

def gamescreen():
   
   #layout
   screen.fill("black")
   screen.blit(board_img,(0,0))
   screen.blit(bar_img,(0,722))
  

   #question
   for i in range(9):
      for j in range(9):
         key=finalgrid[i][j]
         screen.blit(numbers_img[key],(78*i,78*j))

      

   #bar
   i=0
   for num in numbers_img:
      if num!=blank_img:
         screen.blit(num,((78*i),722))
         i+=1

   for m in range(1,10):
      screen.blit(numbers_img[m], dragger[m].rect)
   global timer_value
   timer_value+=1
   draw_timer(timer_value//120)


def levelscreen():
   screen.fill("cyan")
   for button in level_buttons:
      button.process()
   # for butt in newbutton.level_buttons:
   #    butt.process()







   
   


   

   
   
   
   

   
   
   





#buttons
menu_buttons = [
    newbutton.Button(screen, 510, 180, ["red", "blue", "green"], 200, 50, newgamepressed, "New Game"),
    newbutton.Button(screen, 510, 280, ["red", "blue", "green"], 200, 50, myfunction, "Continue"),
    newbutton.Button(screen, 510, 380, ["red", "blue", "green"], 200, 50, myfunction, "Settings"),
    newbutton.Button(screen, 510, 480, ["red", "blue", "green"], 200, 50, myfunction, "Exit")
]

# Buttons for the level screen
level_buttons = [
    newbutton.Button(screen, 510, 180, ["red", "blue", "green"], 200, 50, easypress, "Easy"),
    newbutton.Button(screen, 510, 280, ["red", "blue", "green"], 200, 50, mediumpress, "Medium"),
    newbutton.Button(screen, 510, 380, ["red", "blue", "green"], 200, 50, hardpress, "Hard"),
    newbutton.Button(screen, 510, 480, ["red", "blue", "green"], 200, 50, godmodepress, "God Mode")
]




null=(0,0)
boxprint=0
green=False
red = False

while run==True:

   if logics["showhome"]==True:
      homescreen()
   elif logics["showmenu"]==True:
      menuscreen()
   elif logics["showlevel"]==True:
      levelscreen()
   elif logics["showgame"]==True:  
      gamescreen()

      newbox_printer()
              
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
           

            for i in range(1,10):
               if event.type == pygame.MOUSEBUTTONDOWN:
                  
                  if dragger[i].rect.collidepoint(event.pos):
                     dragger[i].dragging = True

               elif event.type == pygame.MOUSEBUTTONUP :
                  mousepos=pygame.mouse.get_pos()
                  if dragger[i].dragging:
                     dragger[i].dragging = False
                     dragger[i].return_home()
                     for newrect in empty_rect:
                        if  newrect.collidepoint(mousepos):
                           boxprint=i
                           x= newrect.left
                           y= newrect.top
                           if sudokumaker.isvalid(finalgrid,x//78,y//78,i):
                              
                              red = False
                              empty_rect.remove(newrect)
                              filled_rect.append((boxprint,newrect))
                              finalgrid[(x//78)][(y//78)]=i
                           else:
                              red = True
                              

                        
                  

               elif event.type == pygame.MOUSEMOTION:
                  if dragger[i].dragging:
                     dragger[i].rect.move_ip(event.rel)
            
           
            pygame.display.update()
      




   for event in pygame.event.get():
      if event.type==pygame.QUIT:
         run=False
      if event.type==pygame.KEYDOWN:
         if event.key==pygame.K_SPACE:
            for key in logics:
               logics[key] = False
               logics["showmenu"]=True
      
            
            
   
   
   pygame.display.update()
   clock.tick(120)
   
pygame.quit()


