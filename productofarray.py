def check(a,n):
    prod = 1
    flag = 0
    for i in range(n):
        if a[i]==0:
            flag+=1
        else:
            prod*=a[i]

    arr =[0 for i in range(n)]

    for i in range(n):
        if flag>1:
            arr[i] = 0
        elif flag==0:
            arr[i] = prod//a[i]
        elif flag==1 and a[i]!=0:
            arr[i] = 0
        else:
            arr[i] = prod

    return arr


a = [12,0]
n = len(a)
print(check(a,n))