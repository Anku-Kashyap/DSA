def isvalid(li,n,m,mid):
    s = 0
    for i in range(n):
        if li[i]>=mid:
            s+=(li[i]-mid)
            if s>m:
                return False
    return True

n,m = map(int,input().split())
li =  list(map(int,input().split()))
a = min(li)
b = max(li)
res  = -1
while a<=b:
    mid = (a+b)//2
    if isvalid(li,n,m,mid):
        res = mid
        b = mid-1
    else:
        a = mid+1
print(res)

