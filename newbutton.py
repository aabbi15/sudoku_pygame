import pygame
import sys

pygame.init()

xfont = pygame.font.SysFont("Arial", 40)

# menu_buttons=[]
# level_buttons=[]


class Button:

    def __init__(self,screen, x,y,color,width,height,whenclicked,text="button"):
        self.x=x
        self.y=y
        self.color=color
        self.text=text
        self.screen=screen
        self.whenclicked=whenclicked
        self.width=width
        self.height=height

        self.buttonsurface = pygame.Surface((self.width,self.height))
        
        self.textsurface= xfont.render(text,True,"white")
        self.rect= pygame.Rect(self.x,self.y,self.width,self.height)

        self.alreadypressed=False
        
        
    def process(self):
        center =[self.rect.width/2-self.textsurface.get_rect().width/2,self.rect.height/2-self.textsurface.get_rect().height/2]
        self.buttonsurface.blit(self.textsurface,center)
        self.screen.blit(self.buttonsurface,self.rect)

        mousepos=pygame.mouse.get_pos()
        self.buttonsurface.fill(self.color[0])
        if self.rect.collidepoint(mousepos):

            self.buttonsurface.fill(self.color[1])
            if pygame.mouse.get_pressed()[0]:
                self.buttonsurface.fill(self.color[2])
                self.whenclicked()
                self.alreadypressed=True
            else:
                self.alreadypressed=False

class ColorButton:

    def __init__(self,screen, x,y,color,width,height,whenclicked,text,textcolor):
        self.x=x
        self.y=y
        self.color=color
        self.text=text
        self.screen=screen
        self.whenclicked=whenclicked
        self.width=width
        self.height=height

        self.buttonsurface = pygame.Surface((self.width,self.height))
        
        self.textsurface= xfont.render(text,True,textcolor)
        self.rect= pygame.Rect(self.x,self.y,self.width,self.height)

        self.alreadypressed=False
        
        
    def process(self):
        center =[self.rect.width/2-self.textsurface.get_rect().width/2,self.rect.height/2-self.textsurface.get_rect().height/2]
        self.buttonsurface.blit(self.textsurface,center)
        self.screen.blit(self.buttonsurface,self.rect)

        mousepos=pygame.mouse.get_pos()
        self.buttonsurface.fill(self.color[0])
        if self.rect.collidepoint(mousepos):

            self.buttonsurface.fill(self.color[1])
            if pygame.mouse.get_pressed()[0]:
                self.buttonsurface.fill(self.color[2])
                self.whenclicked()
                self.alreadypressed=True
            else:
                self.alreadypressed=False



