def check(arr,n,k):
    c  =0
    arr.sort()
    for i in range(0,n-2):
        l = i+1
        r = n-1
        while l<r:
            if arr[i]+arr[l]+arr[r]==k:
                c+=1
            elif arr[i]+arr[l]+arr[r]<k:
                l+=1
            else:
                r-=1
    return c
        
arr = [1, 4, 45, 6, 10, 8]
k = 13
n = len(arr)
print(check(arr,n,k))