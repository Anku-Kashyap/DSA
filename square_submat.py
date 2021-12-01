mat = [[ 1 , 1 , 1 , 0 ],
        [ 1 , 1 , 1 , 1 ],
        [ 1 , 1 , 0 , 0 ]
        ]

m =  len(mat)
n = len(mat[0])
mx = 0

cache = [[0 for _ in range(n)] for _ in range(m)]

def dfs(mat,i,j,cache):
    if i==m or j==n:
        return 0
    
    if not mat[i][j]:
        return 0
    
    if cache[i][j]>0:
        return cache[i][j]
    
    cache[i][j] =  1+ min(dfs(mat,i+1,j,cache),dfs(mat,i,j+1,cache),dfs(mat,i+1,j+1,cache))
    return cache[i][j]


for i in range(m):
    for j in range(n):
        if mat[i][j] == 1:
            mx = max(mx,dfs(mat,i,j,cache))

print(mx*2)