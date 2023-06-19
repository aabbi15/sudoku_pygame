from pygame.locals import *
import pygame

import sys

pygame.init()




all_draggers = []


class DragnDrop:
    def __init__(self, screen, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.width = image.get_width()
        self.height = image.get_height()
        self.screen = screen
        self.moving=False

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x,self.y)
        self.dragging = False
        # self.rect = pygame.Rect(x, y, self.width, self.height)
        # all_draggers.append(self)

    def return_home(self):
        self.rect.topleft = (self.x,self.y)
        self.screen.blit(self.image, self.rect)

   

    


                


    

    
