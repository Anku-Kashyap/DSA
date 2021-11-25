def check(arr,n):
    s = list(set(arr[0]))
    a = []
    c = 0
    for  i in range(n):
        for j in range(1,n):
            if s[i] in arr[j]:
                c+=1
        if c==n-1:
            a.append(s[i])
        c = 0
    return a




arr =  [[1, 2, 1, 4, 8],[3, 7, 8, 5, 1],[8, 7, 7, 3, 1],[8, 1, 2, 7, 9]]
n = len(arr)
print(*check(arr,n))