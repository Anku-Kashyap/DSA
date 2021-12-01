mat = [[True,False,False],[False,True,False],[False,False,False]]
m = len(mat)
n = len(mat[0])

s = set()
for i in range(m):
    for j in range(n):
        if mat[i][j] == True:
            s.add((i,j))

for i,j in s:
    x,y =  i,j
    while x<m:
        mat[x][y] = True
        x+=1
    
    x,y = i,j
    while y<n:
        mat[x][y] = True
        y+=1

print(mat)



