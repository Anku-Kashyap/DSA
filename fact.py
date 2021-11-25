import sys
import math
def  check(a):
    res=  [None]*500
    res[0] =1 
    result = 1
    x =2
    while x<=a:
        result = multiply(x,res,result)
        x+=1

    

long a = 5
print(check(a))