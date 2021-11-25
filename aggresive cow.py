for _ in range(int(input())):
    n,c = map(int,input().split())
    li = []
    for i in range(n):
        li.append(int(input()))
    li.sort()
    low,high,mid,best = 0, li[n-1],0,0
    while low<=high:
        mid = (low+high+1)//2
        count,left,i = 1,0,1
        while i<n and count<c:
            if li[i]-li[left]>=mid:
                left = i
                count+=1
            i+=1
        
        if count>=c:
            best = mid
            low = mid+1
        
        else:
            high = mid-1
    print(best)