def check(s,n):
    one,zero,count =0,0,0
    for i in range(n):
        if s[i]=='1':
            one+=1
        else:
            zero+=1

        if one==zero:
            count+=1
    return count    
str = "0100110101"
n = len(str)
print(check(str,n))