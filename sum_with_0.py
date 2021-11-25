def  check(arr,n):
    s =  0
    a = set()
    for i in range(n):
        s += arr[i]
        if s==0 or s in a:
            return 'YES'
        a.add(s)
    return 'False'
   
    
arr =[1,2,3,4,5]
n = len(arr)
print(check(arr,n))