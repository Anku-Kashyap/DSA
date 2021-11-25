def check(arr,a,b,n):
    start = 0
    end = n-1
    i = 0
    while i<=end:
        if arr[i]<a:
            arr[i],arr[start] = arr[start],arr[i]
            i+=1
            start+=1
        elif arr[i]>b:
            arr[i],arr[end] = arr[end],arr[i]
            end-=1
        else:
            i+=1


    return arr




arr =[1, 14, 5, 20, 4, 2, 54,
           20, 87, 98, 3, 1, 32]
n = len(arr)
a,b = 10,20
print(check(arr,a,b,n))