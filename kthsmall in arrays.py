def check(a,s,n,m,k):
    i,j,l = 0,0,0

    while i<n and j<m:
        if a[i]<s[j]:
            l+=1
            if l==k:
                return a[i]
            i+=1
        else:
            l+=1
            if l==k:
                return s[j]
            j+=1

    while i<n:
        l+=1
        if l==k:
            return a[i]
        i+=1

    while j<m:
        l+=1
        if l==k:
            return s[j]
        j+=1
    return -1

a =[2, 3, 6, 7, 9]
s =[1, 4, 8, 10]
k  = 5
print(check(a,s,len(a),len(s),k))