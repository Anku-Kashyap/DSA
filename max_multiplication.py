def check(arr,n):
    a = arr[0]
    b = arr[0]
    pro = 1
    for i in range(1,n):
        if arr[i]<0:
            a,b = b,a
        a = max(arr[i],a*arr[i])
        b = min(arr[i],b*arr[i])
        pro = max(pro,a)

    return pro


arr= [-8,5,3,1,6]
n = len(arr)
print(check(arr,n))