def  check(s,a,m,n):
    dp =[[0 for i in range(m+1)] for i in range(n+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i==0:
                dp[i][j] = j
            
            elif  j==0:
                dp[i][j] = i
            
            elif s[i-1]==a[j-1]:
                dp[i][j] = dp[i-1][j-1]

            else:
                dp[i][j] =  1+ min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
        print(dp)
    return dp[m][n]
   

    
s = "geeks"
a = "gesek"
print(check(s,a,len(s),len(a)))