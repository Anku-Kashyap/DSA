def check(s,n):
    a = [[0 for i in range(n)] for i in range(n)]
    i = 0
    max_lenght= 1
    while i<n:
        a[i][i]= True
        i+=1
    
    start= 0
    i = 0
    while  i<n-1:
        if s[i]==s[i+1]:
            a[i][i+1]=True
            start = i
            max_lenght = 2
        i+=1
        
    k= 3
    while k<=n:
        i= 0
        while i<n-k+1:
            j = i+k-1
            if a[i+1][j-1]==True and s[i]==s[j]:
                a[i][j]=True

                if k>max_lenght:
                    start= i
                    max_lenght = k
            i+=1
        k+=1

    return s[start:start+max_lenght]


arr = "aaaabbaa"
n = len(arr)
print(check(arr,n))