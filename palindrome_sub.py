arr= "aaaaaaaaaaaaaaaaaaaaaaaaaaa"
dp = [[-1 for i in range(1000)] for  i in range(1000)]

def check(i,j):
    
    if i>j:
        return 0

    if dp[i][j]!=-1:
        return dp[i][j]
    
    if i==j:
        dp[i][j]=1
        return dp[i][j]
    
    elif arr[i]==arr[j]:
        dp[i][j] = (check(i+1,j)+check(i,j-1)+1)
        return dp[i][j]
    
    else:
        dp[i][j] = (check(i+1,j)+check(i,j-1)-check(i+1,j-1))
    
        return dp[i][j]



n=  len(arr)
print(check(0,n-1))