import pygame
from Polygon import Polygon

def main():
    pygame.init()
    size = (720,480)
    pygame.display.set_caption("Game")
    screen = pygame.display.set_mode(size)

    path = Polygon()
    
    RUN = True
    
    while RUN:      
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                path.vertices.append(event.pos)
                print(event.pos)  
            if event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_RETURN):
                    print("Enter")
                    path.draw(screen)
                
        
        
            if event.type == pygame.QUIT:
                RUN = False
        pygame.display.flip()
main()