def check(a,b,c):
    flag =0
    for i  in range(len(c)):
        if c.count(c[i])!= a.count(c[i])+b.count(c[i]):
            flag=  1
            return False
            
    if flag==0:
        return True



a=  "AB11"
b= "CD2"
c = "ABCD12"
print(check(a,b,c))