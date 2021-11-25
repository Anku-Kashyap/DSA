def  check(arr,k,n):
    count = 0
    for i in range(n):
        if arr[i]<=k:
            count+=1
    
    bad =0
    for i in range(0,count):
        if arr[i]>k:
            bad+=1
    
    ans = bad
    j = count

    for i in range(n):

        if j==n:
            
            break

        if arr[i]>k:
            bad -=1
        
        if arr[j]>k:
            bad+=1
        
        ans = min(ans,bad)
        j+=1
    return ans


arr=  [2, 1,5,6,3,7]
k = 3
n = len(arr)
print(check(arr,k,n))