def check(mat,n):
    m = [ [0]*n for i in range(n)]
    s = []
    for i in range(n):
        s+=mat[i]
    s.sort()
    for i in range(n):
        for j in range(n):
            m[i][j] = s[i*n+j]
    return m


Mat=[[10,20,30,40],
[15,25,35,45] ,
[27,29,37,48] ,
[32,33,39,50]]
n = len(Mat)
print(check(Mat,n))