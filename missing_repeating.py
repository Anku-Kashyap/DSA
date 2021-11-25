def check(a,n):
    b = list(set(a))
    res = (n*(n+1)//2)-sum(b)
    d  = {}
    for i in range(len(a)):
        if a[i] in d.keys():
            return [a[i],res]
        else:
            d[a[i]]=1

a =[12, 7, 5, 1 ,13, 1 ,10, 8, 11, 9, 2, 4, 3, 6]
n = 14
print(check(a,n))