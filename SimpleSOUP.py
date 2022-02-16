import pygame
import random
pygame.init()  
pygame.display.set_caption("easy platformer")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3


#DO be platform :)
class platform:
    def __init__(self, xpos, ypos ):
        self.xpos = xpos
        self.ypos = ypos
        
    def draw(self):
        pygame.draw.rect(screen, (255, 0, 255), (self.xpos, self.ypos, 50, 20))
      
        
    def collide(self, xpos, ypos):
        if xpos+20>self.xpos and xpos<self.xpos+50 and ypos+40>self.ypos and ypos+40<self.ypos+20:
            return self.ypos
        else:
            return False
       
      

p1 = platform(200, 700)
p2 = platform(300, 700)
p3 = platform(400, 700)
p4 = platform(500, 700)

xpos = 300
ypos =300
vx = 0
vy =0
isOnGround = False

keys = [False, False, False, False] #this list holds whether each key has been pressed

while not gameover: #GAME LOOP############################################################
    clock.tick(60) #FPS
    
    #Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
      
        if event.type == pygame.KEYDOWN: #keyboard input p1
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True
                
            if event.key == pygame.K_RIGHT:
                keys[RIGHT]=True

            elif event.key == pygame.K_UP:
                keys[UP]=True
                
                
        elif event.type == pygame.KEYUP:
            if event.key ==  pygame.K_LEFT:
                keys[LEFT]=False

            elif event.key == pygame.K_UP:
                keys[UP]=False
                
            if event.key == pygame.K_RIGHT:
                keys[RIGHT]=False
                
    #physics section--------------------------------------------------------------------
    #RIGHT MOVEMENT
    if keys[RIGHT]==True:
        vx = 3
                   
                
    #LEFT MOVEMENT
    elif keys[LEFT]==True:
        vx = -3
        

    #turn off velocity
    else:
        vx = 0
        #JUMPING
    if keys[UP] == True and isOnGround == True: #only jump when on the ground
        vy = -8
        isOnGround = False
        direction = UP
    
    

    #collision
    isOnGround = False
    if p1.collide(xpos, ypos) !=False:
        isOnGround = True
        vy =0
        ypos = p1.collide(xpos, ypos)-40
    if p2.collide(xpos, ypos) !=False:
        isOnGround = True
        vy =0
        ypos = p2.collide(xpos, ypos)-40
    if p3.collide(xpos, ypos) !=False:
        isOnGround = True
        vy =0
        ypos = p3.collide(xpos, ypos)-40
    if p4.collide(xpos, ypos) !=False:
        isOnGround = True
        vy =0
        ypos = p4.collide(xpos, ypos)-40


    
    #stop falling if on bottom of game screen
    if ypos > 760:
        isOnGround = True
        vy = 0
        ypos = 760
    
    #gravity
    if isOnGround == False:
        vy += .25 #notice this grows over time, aka ACCELERATION
    

    #update player position
    xpos += vx 
    ypos += vy
    
  
    # RENDER Section--------------------------------------------------------------------------------
            
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
      
    pygame.draw.rect(screen, (250, 250, 0), (xpos, ypos, 20, 40))
    
    p1.draw()
    p2.draw()
    p3.draw()
    p4.draw()
    
    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------
pygame.quit()

