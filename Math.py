class Matrix():
    def __init__(self, *args):
        if len(args) == 0: # identity matrix
            self.a = 1
            self.b = 0
            self.c = 0
            self.d = 1
        elif len(args) == 1: # assume input is a matrix e.i copy it
            self.a = args[0].a
            self.b = args[0].b
            self.c = args[0].c
            self.d = args[0].d
        elif len(args) == 2: # assume 2 column vectors
            self.a = args[0][0]
            self.b = args[1][0]
            self.c = args[0][1]
            self.d = args[1][1]
        elif len(args) == 4: # 4 inputs, 4 slots
            self.a = args[0]
            self.b = args[1]
            self.c = args[2]
            self.d = args[3]
        else:
            raise Exception('Unexpected amount of arguments. expect 0, 1 matrix, 2 vectors or 4 values. len(args)={}'.format(len(args)))
    
    def scale(self,x):
        return Matrix(self.a*x,self.b*x,self.c*x,self.d*x)
    def scale_ip(self,x):
        self.a *= x
        self.b *= x
        self.c *= x
        self.d *= x
        return self
    def adj(self):
        return Matrix(self.d,-self.b,-self.c,self.a)
    def adj_ip(self):
        temp = self.a
        self.a = self.d
        self.b = -self.b
        self.c = -self.c
        self.d = temp
        return self
    def det(self):
        return self.a*self.d-self.b*self.c
    def inverse(self):
        return self.adj().scale_ip(1/self.det())
    def inverse_ip(self):
        return self.adj_ip().scale_ip(1/self.det()) 
    def matrix_mult(self,m):
        return matrix(self.a*m.a+self.b*m.c,self.a*m.b+self.b*m.d,self.c*m.a+self.d*m.c,self.c*m.b+self.d*m.d)
    def matrix_mult_ip(self,m):
        temp = self.a
        self.a = self.a*m.a+self.b*m.c
        self.b = temp*m.b+self.b*m.d
        temp = self.c
        self.c = self.c*m.a+self.d*m.c
        self.d = temp*m.b+self.d*m.d
        return self
    def vector_mult(self,v):
        return (self.a*v[0]+self.b*v[1], self.c*v[0]+self.d*v[1])
    def vector_mult_ip(self,v):
        v[0] = self.a*v[0]+self.b*v[1]
        v[1] = self.c*v[0]+self.d*v[1]
    def printSelf(self):
        print(self.a,self.b,self.c,self.d)
    
    
    
    
    