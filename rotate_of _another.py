def  check(a,b):
    temp = a+a
    if temp.count(b)>0:
        return "yes"
    else:
        return "no"


a = "ABACD"
b ="CDABA"
print(check(a,b))