def check(M,n):
    s =[0]*n
    c =0
    a = 0
    for i in range(n):
        for j in range(m):
            if M[i][j]!=0:
                c+=1
                s[j]+=1
            else:
                s[j] = 0
        if a<min(s)*c:
            a=  min(s)*c
        c = 0
    return a        

M  =[[0 ,1 ,1 ,0],
        [1 ,1, 1, 1],
        [1 ,1 , 1,1],
        [1,1,0,0]]
n=  len(M)
print(check(M,n))