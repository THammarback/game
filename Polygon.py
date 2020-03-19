import pygame

class Polygon:   
    def __init__(self,color = (255,255,255)):
        self.vertices = []
        self.color = color
    
    def draw(self, screen):
        for i in range(len(self.vertices)-1):
            pygame.draw.line(screen,self.color, self.vertices[i], self.vertices[i+1])