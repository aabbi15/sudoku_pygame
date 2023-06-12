import pygame
import button


pygame.init()

w= 1200
h=800

#basics
screen = pygame.display.set_mode((w,h))
#screen.fill("cyan")


pygame.display.set_caption("SUDOKU")





#fonts
myfont= pygame.font.SysFont("Arial",70)
# newgame_img= pygame.image.load("newgame.png").convert_alpha()
# continue_img= pygame.image.load("continue.png").convert_alpha()
# exit_img= pygame.image.load("exit.png").convert_alpha()
# settings_img= pygame.image.load("settings.png").convert_alpha()
# #newgame_img= pygame.image.load("newgame.png").convert_alpha()





#logics
gamescreen=False
run = True
menuscreen= False
homescreen=True
settingscreen=False


#buttons

# newgame_butt= button.Button(newgame_img,300,0,0.25)
# continue_butt= button.Button(continue_img,300,150,0.25)
# exit_butt= button.Button(exit_img,300,450,0.25)
# settings_butt= button.Button(settings_img,300,300,0.25)


#functions
def title(text,font,col,x,y):
   img = font.render(text,True,col)
   screen.blit(img,(x,y))

def myfun():
      print("YOu pressed button")


def started():
   screen.fill("red")
   #title ("Game has started",myfont,"red",350,300)
   #pygame.display.flip()
   #print(text)

def display_menu():
    screen.fill("cyan")
#     newgame_butt.draw(screen)
#     continue_butt.draw(screen)
#     exit_butt.draw(screen)
#     settings_butt.draw(screen)

# def click_checker(event):

#     if newgame_butt.isclicked(event)==True:
#             gamescreen=True
#             menuscreen=False
            
#     if continue_butt.isclicked(event)==True:
#             gamescreen=True
#             menuscreen=False
#     if settings_butt.isclicked(event)==True:
#             settingscreen=True
#             menuscreen=False
#     if exit_butt.isclicked(event)==True:
#             homescreen=True
#             menuscreen=False




def game_screen():
        
        title("SUDOKU GAME",myfont,"black",350,10)

def continue_screen():
        title("SUDOKU GAME but continued",myfont,"black",350,10)

def settings_screen():
        title("Settings",myfont,"black",350,10)

def home_screen():
        screen.fill("pink")
        title("Welcome  to  SUDOKU",myfont,"black",350,10)
        # title("To",myfont,"black",400,60)
        # title("SUDOKU",myfont,"black",450,110)
        title("Press SPACEBAR to continue",myfont,"black",30,600)










    





   





#game running
while (run==True):

    screen.fill("white")
    if homescreen:
        home_screen()
    if menuscreen==True:    
        display_menu()
    if gamescreen:
         game_screen()
    if settingscreen:
          settings_screen()
        

    
   

       

    for event in pygame.event.get():

        # click_checker(event)
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE or pygame.K_KP_ENTER:
                menuscreen=True
                homescreen=False
                
                
    

        if event.type ==pygame.QUIT:
            run=False
    
    pygame.display.update()
    
    



pygame.quit()








