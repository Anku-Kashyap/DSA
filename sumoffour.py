def check(a,n,k):
    a.sort()
    s =[]
    for i in range(n-3):
        for j in range(i+1,n-2):
            l = j+1
            r = n-1

            while l<r:
                if a[i]+a[j]+a[l]+a[r]==k:
                    s.append([a[i],a[j],a[l],a[r]])
                    l+=1
                    r-=1
                elif a[i]+a[j]+a[l]+a[r]<k:
                    l+=1
                else:
                    r-=1
    return s
    


a = [0,0,2,1,1]
n = len(a)
k = 3
print(check(a,n,k))