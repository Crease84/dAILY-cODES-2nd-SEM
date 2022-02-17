import pygame
import random
pygame.init()

screen = pygame.display.set_mode((800, 800))

screen.fill((0, 2, 125))
pygame.display.set_caption("CLOUDS??")

class cloudFF7():
    def __init__(self,x,y):
        self.xpos = x
        self.ypos = y
        
    def draw(self):
        pygame.draw.arc(screen, (255, 148, 148), [self.xpos+24, self.ypos, 150, 155], (5*3.1415)/3, 4*3.14/3, 10)
    
        pygame.draw.arc(screen, (255, 203, 148), [self.xpos+12, self.ypos-30, 180, 180],  (5*3.1415)/3, 4*3.14/3, 10)
    
        pygame.draw.arc(screen, (251, 255, 148), [self.xpos, self.ypos-55, 200, 200],  (5*3.1415)/3, 4*3.14/3, 10)
    
        pygame.draw.arc(screen, (155, 255, 148), [self.xpos-10, self.ypos-80, 220, 220],  (5*3.1415)/3, 4*3.14/3, 10)
    
        pygame.draw.arc(screen, (148, 251, 255), [self.xpos-10, self.ypos-80, 220, 220],  (5*3.1415)/3, 4*3.14/3, 10)

        pygame.draw.circle(screen, (255, 255, 255), (self.xpos+50, self.ypos+190), 50, 0)
    
        pygame.draw.circle(screen, (255, 255, 255), (self.xpos+100, self.ypos+170), 50, 0)
    
        pygame.draw.circle(screen, (255, 255, 255), (self.xpos+150, self.ypos+190), 50, 0)
    
        pygame.draw.rect(screen, (255, 255, 255), (self.xpos+50, self.ypos+160, 95, 80))


#instantiate objects
cloudbag = list()
for i in range(10):
    cloudbag.append(cloudFF7(random.randrange(700),random.randrange(700)))

while(True):#game loop!
    
    #render section
    for cloudFF7 in cloudbag:
        cloudFF7.draw()
    pygame.display.flip()



pygame.quit()
