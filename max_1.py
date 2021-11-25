def  check(arr,n,m):
    a,b = 0,0
    for i in range(n):
        c = (arr[i]).count(1)
        if c>a:
            a = c
            b =  i
    if a>0:
        return b
    else:
        return -1



arr = [[0, 1, 1, 1],[0, 0, 1, 1],[1, 1, 1, 1],[0, 0, 0, 0]]
n = len(arr)
m = len(arr[0])
print(check(arr,n,m))