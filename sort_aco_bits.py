def check(a,n):
    d ={}
    for i in range(n):
        d[a[i]] = bin(a[i]).count('1')
    sorted_x = sorted(d.items(), key=lambda kv: kv[1],reverse=True)
    i = 0
    for i in range(n):
        a[i] = sorted_x[i][0]
    return a

a =[5, 2, 3, 9, 4, 6, 7, 15, 32]
n = len(a)
print(check(a,n))