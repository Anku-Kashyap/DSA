for i in range(int(input())):
    n,q = map(int,input().split())
    a,b = map(int,input().split())
    s = [i for i in range(a,b)]
    for j in range(q):
        c  = int(input())
        if c< (b-a):
            print(s[c-1])
        else:
            print(-1)