def merge(arr,temp,left,mid,right):
    i = left
    j = mid+1
    k = left
    inv_count = 0
    
  
    while i<=mid and j<=right:
        if arr[i]<arr[j]:
            temp[k] = arr[i]
            k+=1
            i+=1
        else:
            temp[k] = arr[j]
            inv_count+=(mid-i+1)
            k+=1
            j+=1

    while i<=mid:
        temp[k] = arr[i]
        k+=1
        i+=1
    
    while j<=right:
        temp[k] = arr[j]
        k+=1
        j+=1

    for l in range(left,right+1):
        arr[l] = temp[l]

    return inv_count



def mergeSort(arr,temp,left,right):
    inv_count = 0
    if left<right:
        mid = (left+right)//2

        inv_count+=mergeSort(arr,temp,left,mid)
        inv_count+=mergeSort(arr,temp,mid+1,right)

        inv_count+=merge(arr,temp,left,mid,right)
    
    return inv_count

arr = [2,4,1,3,5]
n = len(arr)
temp = [0]*n
print(mergeSort(arr,temp,0,n-1))
