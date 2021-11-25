def check(a,n):
    r = a[0]
    i =1
    while i<n:
        if a[i]==a[i-1]:
            i+=1
        else:
            r+=a[i]
            i+=1
    return r


a = "aabaa"
n = len(a)
print(check(a,n))