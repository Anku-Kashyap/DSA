def check(arr,n):
    i = n-1
    while i>0:
        if arr[i-1]<arr[i]:
            break
        i-=1
    i = i-1
    j = n-1
    while j>i:
        if arr[j]>arr[i]:
            break
        j-=1
    
    arr[j],arr[i] = arr[i],arr[j]
    arr[i+1:] = sorted(arr[i+1:])
    return arr



arr = [3,2,1]
n = len(arr)
print(check(arr,n))



