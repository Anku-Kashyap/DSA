def mergesort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left =  arr[:mid]
        right = arr[mid:]
        mergesort(left)
        mergesort(right)

        i,j,k = 0,0,0

        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]  = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1

        while i<len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        
        while j<len(right):
            arr[k] = right[j]
            j+=1
            k+=1
    return arr
        


arr = [9,12,1,89,54,34,2,78,90,10]
print("SORTED DATA : " ,*mergesort(arr))