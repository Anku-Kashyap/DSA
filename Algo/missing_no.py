def missing_no(s,n):
    sum_of_n = (n*(n+1))//2
    res =  sum_of_n-sum(s)
    return res

s = [10,2,3,6,1,7,9,8,5]
n = max(s)
print(f"Missing no is {missing_no(s,n)}")

s = [10,4,12,5,7,6,3,2,1,9,8]
n = max(s)
print(f"Missing no is {missing_no(s,n)}")