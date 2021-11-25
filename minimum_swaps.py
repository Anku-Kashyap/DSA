def check(a,n):
    op,cl = 0,0
    swap,imbalance =0,0
    for i in range(n):
        if a[i]=='[':
            op+=1
            if imbalance>0:
                swap+=imbalance
                imbalance-=1
        else:
            cl+=1
            imbalance = (cl-op)
    return swap

a = ['[',']',']','[','[',']']
n = len(a)
print(check(a,n))
