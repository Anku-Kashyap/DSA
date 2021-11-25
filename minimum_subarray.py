import sys

def check(a,n,x):
    s=0
    length = sys.maxsize
    left=  0

    for i in range(n):
        s+= a[i]

        while s>k and left<=i:
            length = min(length,i-left+1)
            s-=a[left]
            left+=1
    return length





arr =[1, 4, 45, 6, 0, 19]
k = 51
n = len(arr)
print(check(arr,n,k))