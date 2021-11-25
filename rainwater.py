def check(arr,n):
    left = [0]*n
    right = [0]*n
    
    left[0] = arr[0]
    for i in range(1,n):
        left[i] = max(left[i-1],arr[i])

    right[n-1] = arr[n-1]
    for i in range(n-2,-1,-1):
        right[i] = max(right[i+1],arr[i])
        print(right)
    water= 0
    for i in range(n):
        water+= min(left[i],right[i])-arr[i]

    return water
    
arr =[8,8,2,4,5,5,1]
n = len(arr)
print(check(arr,n))