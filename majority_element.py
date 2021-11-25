def check(a,n):
    d  = {}
    for i in range(len(a)):
        if a[i] in d.keys():
            d[a[i]]+=1
        else:
            d[a[i]]=1
    for i in range(n):
        if d[a[i]]>n//2:
            return a[i]
    return -1
a  =[3,1,3,3,2]
n = len(a)
print(check(a,n))