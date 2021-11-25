def check(arr,n):
    s = set()
    ans  = 0
    for i in arr:
        s.add(i)

    for i in range(n):
        if (arr[i]-1) not in arr:
            j = arr[i]
            while j in s:
                j+=1
        
            ans = max(ans,j-arr[i])
    return ans
    


arr= [2,6,1]
n = len(arr)
print(check(arr,n))