   gamescreen()
         for event in pygame.event.get():
               if event.type == pygame.QUIT:
                  run = False
               
               if event.type == pygame.MOUSEBUTTONDOWN:
                  
                  if dragger[i].rect.collidepoint(event.pos):
                     dragger[i].dragging = True

               elif event.type == pygame.MOUSEBUTTONUP:
                  dragger[i].dragging = False

               elif event.type == pygame.MOUSEMOTION:
                  if dragger[i].dragging:
                     dragger[i].rect.move_ip(event.rel)
                     gamescreen()
                     pygame.display.update()