def check(arr,k,n):
    for i in range(n):
        if i+1==arr[i]:
            return i+1
            break

arr = [1]
k = 2
n= len(arr)
print(check(arr,k,n))