def mergesort(arr,n):
    temp = [0]*n
    return _mergesort(arr,temp,0,n-1)

def _mergesort(arr,temp,left,right):
    count= 0
    if left<=right:
        mid = (left+right)//2
        count+=_mergesort(arr,temp,left,mid)
        count+=_mergesort(arr,temp,mid+1,right)
        count+= merge(arr,temp,left,mid,right)

    return count

def merge(arr,temp,left,mid,right):
    i = left
    j = mid+1
    k = left
    count = 0

    while i<=mid and j<=right:
        if arr[i]<=arr[j]:
            temp[k] = arr[i]
            i+=1
            k+=1
        else:
            temp[k] = arr[j]
            count += (mid-i+1)
            j+=1
            k+=1
    
    while i<=mid:
        temp[k]  = arr[i]
        i+=1
        k+=1
    while j<=right:
        temp[k] = arr[j]
        k+=1
        j+=1

    for l in range(left,right+1):
        arr[l] = temp[l]
    
    return count


arr = [2,4,1,3,5]
d= len(arr)
print(check(arr,d))