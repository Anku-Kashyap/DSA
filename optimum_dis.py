import  math

class optimum_distance:
    class point:
        def __init__(self,x,y):
            self.x = x
            self.y = y
        
    class Line:
        def __init__(self,a,b,c):
            self.a = a
            self.b = b
            self.c = c

    def dist(self,x,y,p):
        return math.sqrt((x-p.x)**2+(y-p.y)**2)

    
    def compute(self,p,n,l,x):
        res = 0

        y = -1*(l.a*x+l.c)/l.b

        for i in range(n):
            res+=self.dist(x,y,p[i])

        return res
    
    def find_optimum_cost_utill(self,p,n,l):

        low = -1e6
        high = 1e6
        eps  = 1e-6 +1

        while ((high-low)>eps):

            mid1 = low+(high-low)/3
            mid2 = high - (high-low)/3

            dist1 = self.compute(p,n,l,mid1)
            dist2 = self.compute(p,n,l,mid2)

            if dist1<dist2:
                high = mid2
            else:
                low = mid1
        
        return self.compute(p,n,l,(low+high)/2)

    def find_optimum_cost(self,p,l):
        n = len(p)
        p_arr = [None]*n

        for i in range(n):
            p_obj = self.point(p[i][0],p[i][1])
            p_arr[i] = p_obj
        
        return self.find_optimum_cost_utill(p_arr,n,l)
            

if __name__=='__main__':
    obj = optimum_distance()
    l=  obj.Line(1,-1,-3)

    p = [ [ -3, -2 ], [ -1, 0 ],
          [ -1, 2 ], [ 1, 2 ],
          [ 3, 4 ] ]
     
    print(obj.find_optimum_cost(p,l))