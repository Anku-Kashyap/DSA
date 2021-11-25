while True:

    n,*a =  map(int,input().split())

    if n==0:
        break

    m,*b =  map(int,input().split())
    s1,s2,i,j,final= 0,0,0,0,0
    while i<n and j<m:
        if a[i]<b[j]:
            s1+=a[i]
            i+=1
        elif b[j]<a[i]:
            s2+=b[j]
            j+=1
        else:
            final+=max(s1,s2)+a[i]
            s1,s2 = 0,0
            i+=1
            j+=1
    
    while i<n:
        s1+=a[i]
        i+=1
    while j<m:
        s2+=b[j]
        j+=1
    final += max(s1,s2)
    print(final)




