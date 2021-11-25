def  check(n):
    val =""
    res= "1"
    for _ in range(n-1):
        c =1
        for j in range(len(res)-1):
            if res[j]==res[j+1]:
                c+=1
            else:
                val+= str(c)+res[j]
                c = 1
        val+= str(c)+res[-1]
        res = val
        val=""
    return res
        
n = 4
print(check(n))