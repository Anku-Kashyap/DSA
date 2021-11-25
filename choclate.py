def check(A,N,M):
    A.sort()
    a  = []
    for i in range(N-M+1):
        a.appeNd(abs(A[i]-A[i+M-1]))
    return min(a)

A= [7, 3, 2, 4, 9, 12, 56]
m = 3
N = len(A)
print(check(A,N,m))