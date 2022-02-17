import pygame
pygame.init()

screen = pygame.display.set_mode((800, 800))

screen.fill((0, 2, 125))
pygame.display.set_caption("CLOUDS??")

while True:
    
    pygame.draw.arc(screen, (255, 148, 148), [325, 360, 150, 155],  5*3.1415/3, 4*3.14/3, 10)
    
    pygame.draw.arc(screen, (255, 203, 148), [310, 330, 180, 180],  5*3.1415/3, 4*3.14/3, 10)
    
    pygame.draw.arc(screen, (251, 255, 148), [300, 305, 200, 200],  5*3.1415/3, 4*3.14/3, 10)
    
    pygame.draw.arc(screen, (155, 255, 148), [290, 280, 220, 220],  5*3.1415/3, 4*3.14/3, 10)
    
    pygame.draw.arc(screen, (148, 251, 255), [290, 280, 220, 220],  5*3.1415/3, 4*3.14/3, 10)

    pygame.draw.circle(screen, (255, 255, 255), (400, 510), 50, 0)
    
    pygame.draw.circle(screen, (255, 255, 255), (350, 550), 50, 0)
    
    pygame.draw.circle(screen, (255, 255, 255), (450, 550), 50, 0)
    
    pygame.draw.rect(screen, (255, 255, 255), (350, 520, 95, 80))
    
    
    
    pygame.display.flip()

pygame.quit()
