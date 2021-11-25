def  check(n):
    n = str(n)
    r=''
    d  =0
    for i in range(len(n)):
        a = n[d:].count(n[i])
        r+=a
        r+=c[i]
        d+=a
    return r

n = 332251
print(check(n))