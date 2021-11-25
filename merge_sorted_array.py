def nextGap(n):
    if n==1:
        return 0
    return n//2+n%2

def check(a,s,n,m):
    gap =  n+m
    gap = nextGap(gap)
    while gap>0:
        i = 0
        if a[i]>a[i+gap]:
            a[i],a[i+gap] = a[i+gap],a[i]
        i+=1
    
        j = gap-n if gap>n else 0
        while i<n and j<m:
            if a[i]>s[j]:
                a[i],s[j] = s[j],a[i]
            i+=1
            j+=1
    
        if j<m:
            j  =0
            while j+gap<m:
                if s[j]>s[j+gap]:
                    s[j],s[j+gap] = s[j+gap],s[j]

                j+=1
    
        gap = nextGap(gap)



a1 = [10, 27, 38, 43, 82]
a2 = [3, 9]
n = len(a1)
m = len(a2)
check(a1,a2,n,m)
print(a1,a2)