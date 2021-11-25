def check(a,b,c):
    m = []
    for i in range(len(b)):
        k = binary(a,b[i],0,len(a)-1)
        l = binary(c,b[i],0,len(c)-1)
        if k==l and k!=-1 and l!=-1:
            m.append(b[i])

    return m
   
def binary(arr,k,low,high):
    if high>=low:
        mid=(low+high)//2
        if arr[mid]==k:
            return k

        elif k>arr[mid]:
            return binary(arr,k,mid+1,high)

        else:
            return binary(arr,k,0,mid-1)
    
    return -1

a = [1, 5, 5]
b = [3, 4, 5, 5, 10]
c = [5,5, 10, 20]
print(check(a,b,c))