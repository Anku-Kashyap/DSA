d = 256

def check(a,b,q):
    m= len(b)
    n =len(a)
    i,j,p,t= 0,0,0,0
    h = 1
    s =[]

    for i in range(m-1):
        h = (h*d)%q
    
    for i in range(m):
        p = (d*p +ord(b[i]))%q
        t = (d*t +ord(a[i]))%q
    
    for i in range(n-m+1):
        if p==t:
            for j in range(m):
                if a[i+j]!= b[j]:
                    break
                else:
                    j+=1
            
            if j==m:
                s.append(str(i))

        if  i<n-m:
            t = (d*(t-ord(a[i])*h) + ord(a[i+m]))%q

            if t<0:
                t = t+q
    return s
a=  "THIS IS A TEST TEXT"
b = "TEXT"
q = 101
print(*check(a,b,q))