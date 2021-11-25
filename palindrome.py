for  i in range(int(input())):
    n = int(input())
    a = list(input().split())
    flag= 0
    for i in range(n):
        if a[i]!=a[i][::-1]:
            print(0)
            flag=1
            break
    if flag==0:
        print(1)

