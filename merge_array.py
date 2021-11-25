def check(arr):
    n = len(arr)
    ans = 0
    temp = arr.copy()

    h ={}

    temp.sort()
    for i in range(n):
        h[arr[i]] = i
    
    init=i

    for i in range(n):
        if arr[i]!=temp[i]:
            ans+=1
            init = arr[i]

            arr[i],arr[h[temp[i]]] = arr[h[temp[i]]] ,arr[i]

            h[init] = h[temp[i]]
            h[temp[i]] = i
    return ans

arr = [2, 8, 5, 4]
print(check(arr))
