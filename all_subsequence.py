def check(a, res):
    if len(a) == 0:
        print(res, end=" ")
        return
    
    check(a[:-1], res + a[-1])
    check(a[:-1], res)
    return                                                                  



a = "abc"
res= ''
print(check(a,res))