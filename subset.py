
n,a,b = map(int,input().split())
s,sum1,sum2 = [],[],[]
for _ in range(n):
    s.append(int(input()))

powersetsize = 1<<n//2
subSetsize = n//2

for i  in range(powersetsize):
    sum = 0
    for j in range(subSetsize):
        if (i&(1<<j)):
            sum+=s[j]
    sum1.append(sum)

if ((n&1)==1):
    subSetsize = n//2+1
    powersetsize = 1<<subSetsize
else:
    subSetsize = n//2
    powersetsize = 1<<subSetsize

for i in range(powersetsize):
    sum = 0
    for j in range(subSetsize):
        if (i&(1<<j)):
            sum+=s[n//2+j]
    
    sum2.append(sum)

sum1.sort()
sum2.sort()


