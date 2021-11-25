def check(val,weight,W,n):
    s = [[0 for i in range(W+1)] for i in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                s[i][w] = 0
            elif weight[i-1]<=w:
                s[i][w] = max(val[i-1]+s[i-1][w-weight[i-1]],s[i-1][w])

            else:
                s[i][w] = s[i-1][w]

    return s[n][w]


val =[1,2,3]
weight = [4,5,6]
W = 3
n = len(val)
print(check(val,weight,W,n))