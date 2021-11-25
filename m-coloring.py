class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = [[0 for i in range(vertices)] for i in range(vertices
        )]

    
    def issafe(self,v,colour,c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and colour[i]==c:
                return False
        return True
    

    def graphColorUtils(self,m,colour,v):
        if v==self.V:
            return True
        
        for c in range(1,m+1):
            if self.issafe(v,colour,c)==True:
                colour[v] = c

                if self.graphColorUtils(m,colour,v+1):
                    return True
                colour[v]  = 0

    def graphColouring(self,m):
        colour = [0]*self.V
        if self.graphColorUtils(m,colour,0)==None:
            return False
        
        return True


g = Graph(4)
g.graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
m = 3
print(g.graphColouring(m))