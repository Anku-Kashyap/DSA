def merge_sort(v):
    if len(v)==1:
        return 1

    mid = len(v)//2
    L = v[:mid]
    R=  v[mid:]
    merge_sort(L)
    merge_sort(R)

    i,j,k= 0,0,0

    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            v[k]=  L[i]
            i+=1
        else:
            v[k] = R[j]
            j+=1
        k+=1

    while i<len(L):
        v[k] = L[i]
        i+=1
        k+=1
    
    while j<len(R):
        v[k]= R[j]
        j+=1
        k+=1

    if len(v)%2==0:
        return (v[len(v)//2]+v[len(v)//2-1])//2
    else:
        return v[len(v)//2]

v =[56 ,67 ,30 ,79]
print(merge_sort(v))