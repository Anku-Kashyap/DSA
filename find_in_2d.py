class  ABC:
    def __init__(self):
        self.R = None
        self.C = None
        self.dir = [[-1, 0], [1, 0], [1, 1],
                    [1, -1], [-1, -1], [-1, 1],
                    [0, 1], [0, -1]]

    def search(self,grid,row,col,word):
        if grid[row][col]!=word[0]:
            return False
        
        for x,y in self.dir:
            rd,cd = row+x,col+y
            flag=  True

            for k in range(1,len(word)):
                if (0<=rd <self.R and 0<=cd <self.C and word[k]==grid[rd][cd]):
                    rd+=x
                    cd+=y
                else:
                    flag = False
                    break
            
            if flag:
                return True
        return False
    
    def findocc(self,grid,word):
        self.R = len(grid)
        self.C = len(grid[0])
        s  = []
        for row in range(self.R):
            for col in range(self.C):
                if self.search(grid,row,col,word):
                    s.append([row,col])

        return s

grid = [['a', 'b', 'a', 'b'],
        ['a', 'b', 'e', 'b'],
        ['e', 'b', 'e', 'b']]
a = "abe"
b = ABC()
print(b.findocc(grid, a))
