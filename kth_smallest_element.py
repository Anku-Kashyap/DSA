def check(arr,k,n):
    s  =[]
    for i in range(n):
        s+=mat[i]
    s.sort()
    return s[k-1]


arr= [[16, 28, 60, 64],[22, 41, 63, 91],[27, 50, 87, 93],[36, 78, 87, 94]]
k = 3
n= len(arr)
print(check(arr,k,n))