def getminno(a):
    n = len(a)
    lps = [0]*n
    length = 0
    lps[0] =  0
    i = 1
    while i<n:
        if a[i]==a[length]:
            length+=1
            lps[i] = length
            i+=1
        else:
            if length!=0:
                length=  lps[length-1]
            else:
                lps[i]= 0
                i+=1
    return lps[n-1]


def check(a):
    rev = a+a[::-1]
    lps = getminno(rev)
    return len(a)-lps

    
a=  "AACECAAAA"
print(check(a))