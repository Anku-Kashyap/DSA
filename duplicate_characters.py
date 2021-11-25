def check(arr,n):
    d ={}
    for i in arr:
        if i in d.keys():
            d[i]+=1
        else:
            d[i] = 1
    for i in d:
        if d[i]>1:
            print(i,d[i])

arr = "test string"
n = len(arr)
print(check(arr,n))