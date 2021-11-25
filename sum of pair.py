def check(arr,k):
    n = len(arr)
    a = max(arr)
    m =[0]*(a+1)
    c= 0
    for i in range(n):
        m[arr[i]]+=1
    print(m)
    for i in range(n):
        c += m[k-arr[i]]
        if (k-arr[i])==arr[i]:
            c-=1
    return c//2

    
arr = [1,5,7,1]
k = 6
print(check(arr,k))