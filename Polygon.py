from Math import Matrix
from pygame import Vector2 as Vector

class Line:
    def __init__(self,start,end):
        self.start = Vector(start)
        self.end = Vector(end)
        self.vector = self.start-self.end
        
    def printSelf(self):
        print("start: "+str(self.start)+", end: "+str(self.end))
        
    def intersect(self,line):
        try:
            ts = Matrix(self.vector,line.vector).inverse_ip().vector_mult(line.start-self.start)
            if ts[0]<0 and ts[0]>-1 and ts[1]>0 and ts[1]<1:
                a = self.start+self.vector*ts[0]
                return a
        except: #Matrix is not invertable => lines are Parallell => no intersection
            pass
        return False
            


class Polygon:
    def __init__(self,color = (255,255,255)):
        self.vertices = []
        self.color = color
        self.point = (0,0)
        
    def close(self):
        if len(self.vertices) < 2: #cant produce a polygon from 2 points or less => discard
            self.vertices = []
        else:
            self.vertices.append(self.point)
            self.point = False
            self.lines = []
            for i in range(len(self.vertices)):
                self.lines.append(Line(self.vertices[i-1],self.vertices[i]))
            self.lines = tuple(self.lines)
    
    def draw(self, renderer):
        if len(self.vertices) > 0:
            if self.point == False:
                renderer.drawPoly(self.vertices)
            else:
                renderer.drawLines(self.vertices+[self.point])
            
            
    def printSelf(self):
        for vertex in self.vertices:
            print(vertex)
        for line in self.lines:
            line.printSelf()

    def try_merge(self, polygon):
        cps = self.find_collision_points(polygon)
        if len(cps) == 0:
            return False
        elif (len(cps)%2) == 1:
            raise Exception("Odd number of colisions!") #cannot happen
        else:
            return True

         
    def find_collision_points(self, polygon):
        collision_points = []
        for l1 in polygon.lines:
            for l2 in self.lines:
                a = l1.intersect(l2)
                if a:
                    collision_points.append(a)
        return collision_points
            
            
            
            
            
            
                
            