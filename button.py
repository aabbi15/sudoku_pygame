import pygame


class Button():

    def __init__(self,image,x,y,scale):
        width=image.get_width()
        height=image.get_height()
        #self.img = pygame.image.load(path)
        self.image= pygame.transform.scale(image,(int(width*scale),int(height*scale)))
        self.rect= self.image.get_rect()
        self.rect.topleft=(x,y)
        self.clicked=False


    def draw(self,surface):
        
        


        surface.blit(self.image,(self.rect.x,self.rect.y))

        

    def isclicked(self, event):
        mouse_pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(mouse_pos):
                return True

        return False


    

            
        

