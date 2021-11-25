def first(arr,low,high,x,n):
    if high>=low:
        mid = (low+high)//2
        if ((mid==0 or x>arr[mid-1]) and x==arr[mid]):
            return mid
        elif x>arr[mid]:
            return first(arr,mid+1,high,x,n)
        else:
            return first(arr,low,mid-1,x,n)
    return -1

def last(arr,low,high,x,n):
    if high>=low:
        mid = (low+high)//2
        if ((mid==n-1 or x< arr[mid+1]) and x==arr[mid]):
            return mid
        elif x<arr[mid]:
            return last(arr,low,mid-1,x,n)
        else:
            return last(arr,mid+1,high,x,n)
    return -1
    


arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]
x= 5
print(*[first(arr,0,len(arr)-1,x,len(arr)),last(arr,0,len(arr)-1,x,len(arr))])

