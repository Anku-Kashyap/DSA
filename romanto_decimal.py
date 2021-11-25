S  = 'MCMIV'

value = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

p,ans= 0,0
n = len(S)

for i in range(n-1,-1,-1):
    if value[S[i]]>=p:
        ans+=value[S[i]]
    else:
        ans-=value[S[i]]
    p = value[S[i]]
    
print(ans)