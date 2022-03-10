import pygame
import random
pygame.init()  
pygame.display.set_caption("easy platformer")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

SQUARE = [20, 50, 80]

class SQR():
    def __init__(self, x, y, size):
        self.xpos = x
        self.ypos = y
        self.size = size

    def draw(self):
        if self.size == 20:
            C = 80
        if self.size == 50:
            C = 180
        if self.size == 80:
            C = 255
        pygame.draw.rect(screen, (C, 0, C), (self.xpos, self.ypos, self.size, self.size))
    
    def move(self):
        if self.size == 20:
            self.ypos+=1
            C = 80
        if self.size == 50:
            self.ypos+=2
            C = 220
        if self.size == 80:
            self.ypos+=3
            C = 255

    def reset(self):
        if self.ypos > 800:
            self.ypos = (random.randrange(-400, 0))

SQURbag = list()
for i in range(20):
    f = random.randrange(0,3)
    SQURbag.append(SQR(random.randrange(700),(random.randrange(-400, 0)), (SQUARE[f])))
    

while not gameover: #GAME LOOP############################################################
    clock.tick(60) #FPS

    #render section
    screen.fill((0,0,0))

    for SQR in SQURbag:
        SQR.reset()
        SQR.draw()
        SQR.move()
    pygame.display.flip()



pygame.quit()
