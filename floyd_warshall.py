INF = 1000000

def check(,n):
    dist = [[a[i][j] for j in range(n)] for i in range(n)]

    for  k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j]=  min(dist[i][j],dist[i][k]+dist[k][j])
    return dist
matrix = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0,   1],
         [INF, INF, INF, 0]
         ]
n = len(matrix)
print(check(matrix,n))