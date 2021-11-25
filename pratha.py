def isvalid(a,n,p,mid):
    time,pratha = 0,0
    for i in range(n):
        time = a[i]
        j = 2
        while time<=mid:
            pratha += 1
            time+=(a[i]*j)
            j+=1
    if pratha>=p:
        return True
    else:
        return False


for i  in range(int(input())):
    p = int(input())
    n,*arr = map(int,input().split())
    low = 0
    high = 10**7
    while low<=high:
        mid= (low+high)//2
        if isvalid(arr,n,p,mid):
            res = mid
            high = mid-1
        else:
            low = mid+1
    print(res)
