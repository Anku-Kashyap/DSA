def check(a,n):
    s = list(set(a))
    d = []
    for i in range(len(s)):
        d.append(a.count(s[i]))
    d.sort(reverse=True)
    res= 0
    for i in range(len(s)):
        if res>0:
            res = abs(res-d[i])
        else:
            res+=d[i]
    if 0<=res<=1:
        return 1
    else:
        return 0


a = "bbbabaaacd"
n= len(a)
print(check(a,n))