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
        self.rect.topleft = (x,y)
        self.moving = False
        # self.rect = pygame.Rect(x, y, self.width, self.height)
        # all_draggers.append(self)

    def draw_image(self):
        self.screen.blit(self.image, self.rect)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False

            elif event.type == MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.moving = True

            elif event.type == MOUSEBUTTONUP:
                self.moving = False

            elif event.type == MOUSEMOTION and self.moving:
                self.rect.move_ip(event.rel)

        # pygame.display.update()


    def update(self):
        pass

    
# all_draggers=[]

# class DragnDrop():

#     def __init__(self,screen,image,x,y):
#         self.image=image
#         self.x=x
#         self.y=y
#         self.width=image.get_width()
#         self.height=image.get_height()
#         self.screen=screen
#         self.dragging = False

#         self.rect=pygame.Rect(x,y,self.width,self.height)
#         # self.rect.topleft= (x,y)
#         all_draggers.append(self)


#     def draw_image(self,visible):
#         if visible:
#             self.screen.blit(self.image,self.rect)

#     def main(self):
#         # dragging=False

#         # for event in pygame.event.get():
#         #     if event.type==pygame.QUIT:
#         #         run=False

#         #     if event.type==pygame.MOUSEBUTTONDOWN:
#         #         if event.button==1:
#         #             if self.rect.collidepoint(event.pos):
#         #                 self.dragging=True
#         #                 self.offset = event.pos[0] - self.rect.x, event.pos[1] - self.rect.y

#         #     if event.type == pygame.MOUSEBUTTONUP:
#         #         self.dragging = False
                
#         #     if event.type== pygame.MOUSEMOTION:
#         #         if self.dragging:
#         #             # self.rect.move_ip(event.rel)
#         #             self.rect.x = event.pos[0] - self.offset[0]
#         #             self.rect.y = event.pos[1] - self.offset[1]
        
#         # self.drawimage(visible)
#         # pygame.display.update()

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if event.button == 1:
#                     if self.rect.collidepoint(event.pos):
#                         self.dragging = True
#                         self.offset = event.pos[0] - self.rect.x, event.pos[1] - self.rect.y

#             if event.type == pygame.MOUSEBUTTONUP:
#                 if event.button == 1:
#                     self.dragging = False

#             if event.type == pygame.MOUSEMOTION:
#                 if self.dragging:
#                     self.rect.x = event.pos[0] - self.offset[0]
#                     self.rect.y = event.pos[1] - self.offset[1]

#         self.draw_image(True)
        

