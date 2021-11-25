def check(arr,n):
    res,op,cl =0,0,0
    for i in range(n):
        if arr[i]=="}":
            cl +=1
            if op>0:
                op-=1
                cl-=1
        else:
            op+=1
    op,cl = min(op,cl),max(op,cl)
    res += op*2
    cl-=op
    if cl%2!=0:
        return -1
    else:
        res+=cl//2
        return res
        

arr = "{{}{{{}{{}}{{"
n = len(arr)
print(check(arr,n))