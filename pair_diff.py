def binary(arr,res,low,high):
    if low<=high:
        mid = (low+high)//2
        if arr[mid]==res:
            return arr[mid]
        elif res>arr[mid]:
            return binary(arr,res,mid+1,high)
        else:
            return binary(arr,res,low,mid-1)

def check(arr,l,n):
    res = 0
    for i in range(l):
        res = n + arr[i]
        var = binary(arr,res,0,l-1)
        if var!=None:
            return arr[i],var
    return -1

arr=  [90, 70, 20, 80, 50]
l = len(arr)
n = 45
print(check(arr,l,n))