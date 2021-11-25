


dp = [-1 for i in range(10)]

def  check(n):
    if n<=1:
        return n
    global dp

    first,second = 0,0

    if dp[n-1]!=-1:
        first = dp[n-1]
    else:
        first = check(n-1)
    print(dp,n)
    if dp[n-2]!=-1:
        second = dp[n-2]
    else:
        second = check(n-2)
    dp[n] = first+second

    return dp[n]
n = 9
print(check(n))