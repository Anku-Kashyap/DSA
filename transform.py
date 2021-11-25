def check(a,b):
    n = len(a)
    m = len(b)
    if n!=m:
        return False
    
    res = 0
    i,j= n-1,m-1
    while i>=0:
        while i>=0  and a[i]!=b[j]:
            i-=1
            res+=1
        if i>=0:
            i-=1
            j-=1
    return res



A = "ABD"
B = "BAD"
print(check(A,B))