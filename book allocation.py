def isvalid(a,n,m,mid):
    student = 1
    s = 0
    for i in range(n):
        if a[i]>mid:
            return False
        
        if s+a[i]>mid:
            student+=1
            s=  a[i]
        
            if student>m:
                return False
        else:
            s+=a[i]
    return True

    
        

def check(a,n,m):
    if n<m:
        return -1
    start = 0
    end = sum(a)
    res = 10**9
    while start<=end:
        mid = (start+end)//2
        if isvalid(a,n,m,mid):
            res = mid
            end = mid-1
        else:
            start = mid+1
    return res


a = [12,34,67,90]
n = len(a)
m = 2
print(check(a,n,m))