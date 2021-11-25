def binarysearch(arr,n,k):
    mid = n//2
    if  arr[mid]==k:
        return mid
    elif k>arr[mid]:
        return binarysearch(arr,mid+1,k)
    else:
        return binarysearch(arr,mid,k)

arr = [9,12,1,89,54,34,2,78,90,10]
n = len(arr)
k = 34
print(f"Index of {k} is",binarysearch(arr,n,k))