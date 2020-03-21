import pygame
import time
from Polygon import Polygon
from Renderer import Renderer

def main():
    title = "Game!"
    target_fps = 60
    pygame.init()
    size = (720,480)
    renderer = Renderer(size)

    polygons = []
    current_polygon = Polygon()
    
    prev_time = time.time()
    RUN = True
    while RUN: 
        for polygon in polygons:
            polygon.draw(renderer)

        current_polygon.draw(renderer)
        renderer.update()
    
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                current_polygon.point = event.pos

            if event.type == pygame.MOUSEBUTTONDOWN:
                current_polygon.vertices.append(event.pos)
                
            if event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_RETURN):
                    current_polygon.close()
                    
                    #merges overlapping polygons, removeing them from the list of polygons and adding the new merged polygon
                    polygons = list(filter(lambda polygon:not current_polygon.try_merge(polygon) ,polygons))
                    polygons.append(current_polygon)
                    
                    current_polygon = Polygon()
                    
            if event.type == pygame.QUIT:
                RUN = False

        curr_time = time.time()
        diff = curr_time - prev_time
        delay = max(1.0/target_fps - diff, 0)
        time.sleep(delay)
        fps = 1.0/(delay + diff)
        prev_time = curr_time
        pygame.display.set_caption("{0}: {1:.2f}".format(title, fps))

main()
