def check(a,n):
    hashmap = {}
    out =[]
    sum1= 0
    for i in range(n):
        sum1+=a[i]

        if sum1==0:
            out.append((0,i))
        al =[]

        if sum1 in hashmap:
            al = hashmap.get(sum1)
            for it in range(len(al)):
                out.append((al[it]+1,i))
        al.append(i)
        hashmap[sum1] = i
    return out

a= [0,0,5,5,0,0]
n = len(a)
print(check(a,n))