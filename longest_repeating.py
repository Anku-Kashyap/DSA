def check(a):
    n = len(a)
    d = [[0 for i in range(n+1)] for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,n+1):
            if a[i-1]==a[j-1]  and i!=j:
                d[i][j] = 1+ d[i-1][j-1]
            else:
                d[i][j] = max(d[i][j-1],d[i-1][j])
    return d[n][n]

a ="aab"
print(check(a))