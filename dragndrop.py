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

    # def handle_events(self):
    #     for event in pygame.event.get():
    #         if event.type == QUIT:
    #             self.running = False

    #         elif event.type == MOUSEBUTTONDOWN:
    #             if self.rect.collidepoint(event.pos):
    #                 self.moving = True

    #         elif event.type == MOUSEBUTTONUP:
    #             self.moving = False
    #             self.return_home()

    #         elif event.type == MOUSEMOTION and self.moving:
    #             self.rect.move_ip(event.rel)

    def dropped(self,empty_coordinates,run):
        for event in pygame.event.get():
            if event.type ==QUIT:
                run=False
            
            elif self.dragging==False:
                for null in empty_coordinates:
                    if self.rect.collidepoint(null):
                        self.screen.blit(self.image, null)


                


    

    
