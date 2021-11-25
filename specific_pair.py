def check(arr,n):
    mi,mx =0,0
    for i in range(n):
        for j in range(0,i):
            if arr[i][j]<mi:
                mi = arr[i][j]
            if arr[i][j]>mx:
                mx = arr[i][j]
    return mx-mi


arr= [[1, 2, -1, -4, -20 ],[ -8, -3, 4, 2, 1],[3, 8, 6, 1, 3 ],[-4, -1, 1, 7, -6],[0, -4, 10, -5, 1]]
n = len(arr)
print(check(arr,n))