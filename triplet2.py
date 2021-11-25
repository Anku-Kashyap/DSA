def check(a,n,x):
    a.sort()
    ans =0
    for i in range(n-2):
        j = i+1
        k = n-1
        while j<k:
            if a[i]+a[j]+a[k]>=x:
                k-=1
            else:
                ans+=(k-j)
                j+=1

    return ans

a = [5, 1, 3, 4, 7]
x = 12
n = len(a)
print(check(a,n,x))