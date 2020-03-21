import pygame

class Renderer:
    def __init__(self,size):
        self.screen = pygame.display.set_mode(size)
        self.background = pygame.Surface(size).convert()
        self.background.fill((0, 0, 0))

    def drawPoint(self,p):
        pygame.draw.circle(self.screen,(255,0,0) ,p ,int(5))
        

    def drawPoly(self, vertices):
        pygame.draw.polygon(self.screen, (255,255,255,0.5), vertices)

    def drawLines(self, vertices):
        pygame.draw.lines(self.screen, (255,255,255), False, vertices)

    def update(self):
        pygame.display.flip()
        self.screen.blit(self.background, (0, 0))
        
        