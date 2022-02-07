import pygame
pygame.init()


screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Silly Shapes")

while True:
    
    pygame.draw.ellipse(screen, (255, 17, 0), (200, 100, 20, 40))
   
    pygame.draw.rect(screen, (255, 145, 0), (400, 400, 20, 20))
    
    pygame.draw.polygon(screen, (225, 255, 0), ((100, 100), (150, 200), (200, 200)))
    
    pygame.draw.circle(screen, (77, 255, 0), (100, 71), 11, 0)
    
    pygame.draw.arc(screen, (0, 255, 136), [100, 100, 150, 150], 0, 3.1415/2, 10)
    
    pygame.draw.line(screen,(0, 208, 255),(100, 450),(450,450),(3))
    
    pygame.display.flip()

pygame.quit()
