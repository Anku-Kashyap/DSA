li = [[1,4,7],[2,5,8],[3,6,9]]
res= []


def merge(a,b):
    m = len(a)
    n = len(b)
    temp  =[0]*(m+n)
    i,j,k = 0,0,0
    while i<m and j<n:
        if a[i]<b[j]:
            temp[k] = a[i]
            i+=1
        else:
            temp[k] = b[j]
            j+=1
        k+=1
    
    while i<m:
        temp[k] = a[i]
        i+=1
        k+=1
    
    while j<n:
        temp[k] = b[j]
        j+=1
        k+=1
    
    return temp


m = len(li)
res = merge(li[0],li[1])

for i in range(2,m):
    res = merge(res,li[i])

print(res)









