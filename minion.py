def check(s, k):
    a = len(s)//k
    d = list(set(s)) 
    li = []
    for i in range(len(d)):
        if s.count(d[i])>a:
            li.append(d[i])

    return li


s= [3, 1, 2, 2, 1, 2, 3, 3]
k = 4
print(check(s,k))